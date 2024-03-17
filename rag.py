import os
import requests
from openai import OpenAI
from dotenv import load_dotenv
from qdrant_client import models, QdrantClient
from sentence_transformers import SentenceTransformer

load_dotenv()
HOST = os.getenv("QDRANT_HOST")
PORT = os.getenv("QDRANT_PORT")
DB_NAME = os.getenv("QDRANT_DB_NAME")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
TRAVERSAAL_API_KEY = os.environ.get("TRAVERSAAL_API_KEY")

class Rag:
    def __init__(self):
        self.encoder = SentenceTransformer("all-MiniLM-L6-v2")
        self.qdrant = QdrantClient(HOST, port=PORT)
        self.client = OpenAI(
            api_key=OPENAI_API_KEY,
        )
        self.chat_history_list = []
    
    def generate_search_hotel_prompt(self, query, chat_history):
        prompt = f"""You are an AI assisting with hotel-related queries. Consider the entire chat history to understand the context of the user's current needs and preferences. For each query, decide if a search for hotels is needed based on criteria such as location, amenities, or availability. Respond only with "YES" if the query indicates the user is looking for hotels based on new criteria or has not found a satisfactory option yet. Respond with "NO" if the query does not require searching for hotels or the user's needs have already been adequately addressed in the chat history.

        -- Chat History --
        {chat_history}

        -- For example --
        - Query: "I need a hotel in New York for next weekend." Response: "YES"
        - Query: "What kind of facilities does The Grand Resort offer?" Assuming The Grand Resort was previously discussed and the question relates to further details about it, Response: "NO"

        Given the latest query: "{query}", considering the chat history, should a hotel search be conducted? Respond with "YES" or "NO".
        """
        return prompt

    
    def generate_find_info_prompt(self, query, chat_history):
        prompt = f"""Consider the following chat history and the latest query to decide if more specific information about a hotel is required. Information might include details like reviews, services, or detailed descriptions. If the chat history already provides sufficient information or the query does not ask for specific hotel details, respond "NO". If the query asks for specific information not covered in the chat history, respond "YES".

        -- Chat History --
        {chat_history}
        
        -- Latest Query --
        "{query}"

        Based on the chat history and the latest query, is there a need to find more specific information about a hotel? Respond with "YES" or "NO".
        """
        return prompt
    
    def generate_traversaal_search_prompt(self, chat_history, current_query):
        prompt = f"""Consider the following chat history between a user and an AI, and the latest query from the user. Your task is to synthesize the information and generate a single, focused search query that can be used to find additional information relevant to the user's current interest. This search query will be used with an internet search API to retrieve detailed responses and URLs related to the query. Your response should be a concise and relevant search query based on the chat history and the latest query.

        -- Chat History --
        {chat_history}
        
        -- Latest Query --
        "{current_query}"
        
        Based on the chat history and the latest query, generate a search query for additional information:
        """
        return prompt
    
    def generate_hotel_search_result_prompt(self, query, hits):
        # Including a generalized consideration of chat history in the prompt
        prompt = f"""Given the user's query: '{query}' and considering the entire conversation history, including any specific preferences or previously mentioned hotels, choose the best hotel from the list below. Provide a detailed explanation for your choice, ensuring it aligns with the user's needs.
        
        -- Hotel Details --
        {hits}
        
        Considering the conversation history and the details provided, your hotel choice and explanation:
        """
        return prompt

    
    def generate_chat_response_prompt(self, query, chat_history, traversaal_output):
        prompt = f"""You are an AI chatbot trained to assist users by providing helpful and conversational responses. Based on the given chat history, a user's query, and detailed information retrieved from an internet search, your task is to synthesize a chat response that communicates the key information in a friendly and concise manner. The response should reflect the conversational tone of a chat and be informative, directly addressing the user's query with the information provided.

        -- User's Query --
        "{query}"
        
        -- Chat History --
        {chat_history}
        
        -- Information Retrieved from Internet Search --
        {traversaal_output['response_text']}
        
        -- Web URLs for Further Reading --
        {traversaal_output['web_url']}
        
        Generate a chat response that incorporates the key information provided, ensuring it is conversational and informative to the query starting now:
        """
        return prompt
    
    def generate_prompt_based_on_history(self, query, chat_history):
        prompt = f"""As an AI trained to provide accurate and helpful responses, your task is to analyze the provided chat history and the latest user query to generate an informed response. Use the context and details from the chat history to address the user's query directly. You should not assume or infer information not contained in the chat history but may use general knowledge where appropriate.

        -- Chat History --
        {chat_history}
        
        -- Latest Query --
        "{query}"
        
        Based on the chat history and the latest query, generate a response that is informative and directly relevant to the query:
        """
        return prompt
    
    def traversaal_search(self, query):
        url = "https://api-ares.traversaal.ai/live/predict"

        payload = { "query": [f"{query}"] }
        headers = {
        "x-api-key": f"{TRAVERSAAL_API_KEY}",
        "content-type": "application/json"
        }
        
        return requests.post(url, json=payload, headers=headers).json()["data"]

    def qdrant_search(self, query):
        hits = self.qdrant.search(
            collection_name=DB_NAME,
            query_vector=self.encoder.encode(query).tolist(),
            limit=5,
        )
        result = ""
        for hit in hits:
            result += f"Hotel name: {hit.payload['hotel_name']}\nAdditional information: {hit.payload['combined_description']}\n\n"
            
        return result

    def llm_model(self, prompt):
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0,  # 0 is good
            max_tokens=3000,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )
        return response.choices[0].message.content

    def chat(self, query):
        chat_history_str = "\n\n".join(self.chat_history_list)
        need_search_hotel_prompt = self.generate_search_hotel_prompt(query, chat_history_str)
        need_search_hotel = self.llm_model(need_search_hotel_prompt)
        if need_search_hotel == "YES":
            self.chat_history_list = []
            chat_history_str = "\n\n".join(self.chat_history_list)
            hits = self.qdrant_search(query)
            prompt = self.generate_hotel_search_result_prompt(query, hits)
        else:
            need_search_info_prompt = self.generate_find_info_prompt(query, chat_history_str)
            need_search_info = self.llm_model(need_search_info_prompt)
            if need_search_info == "YES":
                traversaal_prompt = self.generate_traversaal_search_prompt(chat_history=chat_history_str, current_query=query)
                traversaal_output = self.traversaal_search(
                    self.llm_model(traversaal_prompt)
                )
                prompt = self.generate_chat_response_prompt(query, chat_history_str, traversaal_output)
            else:
                prompt = self.generate_prompt_based_on_history(query, chat_history_str)
                
            
        response = self.llm_model(prompt)
        self.chat_history_list.append(f"Human: {query}\nAssistant: {response}\n")
        if len(self.chat_history_list) > 10:
            _ = self.chat_history_list.pop(1)
        return response
    
    

if __name__ == "__main__":
    
    rag = Rag()
    while True:
        user_input = input("Human: ")
        response = rag.chat(user_input)
        print(f"AI: {response}")
        print()