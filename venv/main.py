"""""
main.py
17.03.2025

load .env file and extract OPENAI_API
"""""

import os

from dotenv import load_dotenv, find_dotenv
from openai import OpenAI

load_dotenv()

OPEN_API_KEY = os.getenv("OpenAI_API_KEY")


#Parameters
QUESTION = "What is the capital of Hungary?"
SYSTEM_PROMPT = "You are a helpful assistant that can answer that can aswer questions"

MODEL = "gpt-4o-mini"

load_dotenv(find_dotenv(), override=True)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

print(OPEN_API_KEY)
