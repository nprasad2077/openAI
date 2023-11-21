import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.environ.get('OPEN_AI_KEY')

print(api_key)
