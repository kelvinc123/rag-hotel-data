# iSEArch Hotels Project

iSEArch Hotels is a Retrieval-Augmented Generation (RAG) hotel search chatbot that leverages Qdrant for enhanced semantic search capabilities, integrating OpenAI for natural language understanding and Traversaal.ai API for dynamic content retrieval.

## Awards and Recognition 🏅

We are proud to announce that our iSEArch Hotels Project achieved 2nd place in a hackathon organized by Traversaal.ai, competing against 44 participants. This recognition highlights our team's dedication to leveraging innovative technology integrations to develop a state-of-the-art hotel chatbot.

## Getting Started

### Prerequisites
- Ensure **Docker** is installed on your PC. Installation instructions can be found at [Docker's official documentation](https://docs.docker.com/engine/install/).

### Installation Steps

1. **Set Up Your Environment**
   - Clone this repository to your local machine.
   - Create and activate a virtual environment:
     ```bash
     python -m venv venv
     # On macOS/Linux
     source venv/bin/activate
     # On Windows
     .\venv\Scripts\activate
     ```
   - Install required Python dependencies:
     ```bash
     pip install -r requirements.txt
     ```

2. **Run Qdrant**
   - For macOS/Linux, execute:
     ```bash
     ./run_qdrant.sh
     ```
   - For Windows, replicate the commands inside `run_qdrant.sh` in your command prompt.

3. **Environment Configuration**
   - Obtain an **OpenAI API key** and a **Traversaal API key**.
   - Put these API keys along with any other necessary configurations inside the `.env` file located in the project's root directory.

4. **Data Preprocessing and Database Initialization**
   - Prepare your dataset and initialize the Qdrant database with:
     ```bash
     python preprocess.py
     python store_to_qdrant.py
     ```

## Launch the Streamlit Application
Launch the Streamlit app to interact with the chatbot:
```bash
streamlit run streamlit_app.py
```

## Additional Information
 - To directly interact with the chatbot logic or for debugging, run `python rag.py`.
 - For an illustrative example of a user-chatbot interaction, refer to `example_interaction.txt`.


## Example Interaction

A detailed example showcasing the chatbot's interaction with a user, including handling various hotel-related queries, is available in `example_interaction.txt`. This provides insight into the chatbot's capabilities and response quality.
