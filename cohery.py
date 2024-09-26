import cohere
from dotenv import load_dotenv
import os

def summarize_conversation(conversation: str) -> str:
    # Load environment variables
    load_dotenv()
    
    # Get Cohere API key
    cohere_api_key = os.getenv('cohere_API_KEY')

    # Raise an error if the API key is not found
    if not cohere_api_key:
        raise ValueError("Cohere API key is not set in the environment variables!")
    
    # Initialize Cohere client
    co = cohere.Client(cohere_api_key)
    
    # Call the summarize function on the input conversation
    response = co.summarize(
        text=conversation, 
        length='long', 
        format='paragraph', 
        model='summarize-xlarge',
        temperature=0.5
    )
    
    # Return the summary
    return response.summary

# Example usage:
# conversation_text = "Your conversation text here..."
# print(summarize_conversation(conversation_text))
