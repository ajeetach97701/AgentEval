from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())




groq_api_key = os.getenv("GROQ_API")

llm = ChatGroq(api_key=groq_api_key,
                model="mixtral-8x7b-32768",
                temperature=0,
                max_tokens=None,
                timeout=None,
                max_retries=2
                )