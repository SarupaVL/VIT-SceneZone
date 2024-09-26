import re
import pandas as pd
import openai
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Function to parse WhatsApp chat
def parse_whatsapp_chat(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        chat_data = file.readlines()

    # Regex to extract timestamp, sender (phone number), and message
    pattern = r'\[(\d{1,2}:\d{2} [ap]m), (\d{1,2}/\d{1,2}/\d{4})\] (\+[\d ]+): (.*)'
    chat_list = []

    for line in chat_data:
        match = re.match(pattern, line)
        if match:
            time, date, sender, message = match.groups()
            timestamp = f"{date} {time}"  # Combine date and time into one
            chat_list.append({'timestamp': timestamp, 'sender': sender, 'message': message})

    return pd.DataFrame(chat_list)

# Test the function
chat_df = parse_whatsapp_chat('dataaaa.txt')
print(chat_df.head())  # Check the parsed data

# Function to call GPT-4 API for summarization (standard 8k token version)
def summarize_conversation(conversation_chunk):
    api_key = os.getenv('OPENAI_API_KEY')
    
    if not api_key:
        raise ValueError("OpenAI API key not found. Please set it in the environment variables.")
    
    openai.api_key = api_key

    # Create a list of messages in the format expected by the Chat API
    messages = [
        {"role": "system", "content": "You are a helpful assistant that summarizes WhatsApp conversations."},
        {"role": "user", "content": f"Summarize the following WhatsApp conversation while keeping the important points, preserving timestamps, and identifying who said what:\n\n{conversation_chunk}"}
    ]

    # Use GPT-4 (8k tokens limit)
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",  # GPT-4 with 8k tokens limit
        messages=messages,
        max_tokens=4000,    # Adjust this based on desired output length
        temperature=0.7,    # Adjust temperature for creativity control
    )

    return response['choices'][0]['message']['content']

# Chat Data
chat_segment = '\n'.join([f"{row['timestamp']} - {row['sender']}: {row['message']}" for _, row in chat_df.iterrows()])

# Generate Summary using GPT-4 (8k version)
summary = summarize_conversation(chat_segment)
print(summary)
