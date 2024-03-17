"""to preprocess the data to documents.json"""
import json
from dotenv import load_dotenv
import pandas as pd
from datasets import load_dataset

load_dotenv()
#### Preproces data
dataset = load_dataset("traversaal-ai-hackathon/hotel_datasets")
df=pd.DataFrame(dataset['train'])

review_df = df.groupby('hotel_name')["review_title"].agg(lambda x: "\n".join(x))
df_hotel = df[["hotel_name", "hotel_description", "locality", "country", "street_address", "review_count", "rating_value", "price_range"]].drop_duplicates().fillna("")
df_hotel.set_index("hotel_name", inplace=True)
df_hotel["reviews"] = review_df
df_hotel.reset_index(inplace=True)
df_hotel["combined_description"] = "The hotel name is: " + df_hotel["hotel_name"] + ". The hotel description is: " + df_hotel["hotel_description"] + ". This hotel has overall rating of " + df_hotel["rating_value"].apply(lambda x: str(x)) + ". This hotel is located at " + df_hotel["locality"] + " and " + df_hotel["country"] + ". Its address is " + df_hotel["street_address"] + ", the review count is " + df_hotel["review_count"].apply(lambda x: str(x)) + ", the price range is " + df_hotel["price_range"] + ", These are a collection of the reviews of the hotel: " + df_hotel["reviews"]

df_documents = df_hotel[["hotel_name", "combined_description"]]
documents = df_documents.to_dict(orient="records")

with open("documents.json", "w") as f:
    json.dump(documents, f)
