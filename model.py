from dotenv import load_dotenv
load_dotenv()
import os
deep_val_api_key = os.getenv("DEEP_VAL_API_KEY")
groq_api_key = os.getenv("GROQ_API")
from deepeval.models import DeepEvalBaseLLM



CRITIC_MODEL = "llama3-70b-8192"

from langchain_groq import ChatGroq
from langchain.memory import ConversationBufferMemory

"""First install these things before running this file:
1. langchain_groq
2. python-dotenv
"""
from langchain_core.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)

from langchain_groq import ChatGroq

import os
from langchain.prompts import ChatPromptTemplate, PromptTemplate
from dotenv import load_dotenv
from langchain.chains import LLMChain
load_dotenv()


llm = ChatGroq(api_key=groq_api_key,
                        #   model="mixtral-8x7b-32768",
                          temperature=0,
                          max_tokens=None,
                          timeout=None,
                          max_retries=2)


client = llm




def predict(query: str, model: str, client: ChatGroq = client):

    template = ChatPromptTemplate(
        messages=[
            SystemMessagePromptTemplate.from_template("You are a chatbot who has a conversation with human. Do not use any other details from your knowledge base, answer only realted queries."),
            # The `variable_name` here is what must align with memory
            # MessagesPlaceholder(variable_name="chat_history"),
            HumanMessagePromptTemplate.from_template("{question}")
        ]
        )
    conversation = LLMChain(
        llm=llm,
        prompt=template,
        verbose=True,
    )
    response = conversation.invoke({"question":query})
    print(response);print();print()
    return response['text']




from typing import Optional, List
from abc import ABC
import openai
import asyncio
class GroqCriticModel(DeepEvalBaseLLM):
    def __init__(self, model: str):
        self.model = model

    def load_model(self):
        pass

    def generate(self, prompt: str) -> str:
        return predict(prompt, self.model)

    async def a_generate(self, prompt: str) -> str:
        return self.generate(prompt)

    def get_model_name(self):
        return self.model
loaded_model:DeepEvalBaseLLM = GroqCriticModel(model="llama3-70b-8192")


from langchain_ollama.chat_models import ChatOllama
from langchain_ollama import OllamaLLM


from langchain_groq import ChatGroq

def get_model(name = ["groq", "ollama"], ollama_name = []):
    if name == "groq":
        return ChatGroq(
    api_key=groq_api_key,
    temperature=0,
    max_tokens=None,
    timeout=30,  # Ensure timeout is set
    max_retries=2
)
    elif name == "ollama":
        return OllamaLLM(model="llama3")
