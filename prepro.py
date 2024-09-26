import re
import pandas as pd

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
