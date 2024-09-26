import openai
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Set the OpenAI API key from an environment variable
openai.api_key = os.getenv('OPENAI_API_KEY')

if not openai.api_key:
    raise ValueError("OpenAI API key not found. Please set it in the environment variables.")

# List available models
models = openai.Model.list()

# Print model IDs
for model in models['data']:
    print(model['id'])
