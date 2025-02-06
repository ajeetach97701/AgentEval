import os
import pprint
from pydantic import BaseModel, Field
from dotenv import load_dotenv, find_dotenv
from langchain.tools import Tool,StructuredTool
from langchain.schema.runnable import RunnableMap
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.output_parsers.json import JsonOutputParser
from langchain.agents import create_tool_calling_agent, AgentExecutor
string_parser= StrOutputParser()
json_parser = JsonOutputParser()

from langchain.evaluation import load_evaluator


from Agent.model import llm

evaluator = load_evaluator("trajectory", llm =llm)

from Agent.tools import *
from eval_it import get_agent_evaluation

def generate_response(query:str):
    
    prompt_agent = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                f"""
                You are a good assistant. """
            ),
            ("placeholder", "{chat_history}"),
            ("human", "{query}"),
            ("placeholder", "{agent_scratchpad}"),
        ],
    )
    senderId = "senderId"
    tools  = [leadTool, colorTool, greetingsTool]       
    agent = create_tool_calling_agent(llm, tools, prompt_agent)


    agent_executor_instance = AgentExecutor(tools=tools,
                                    return_intermediate_steps=True,
                                    handle_parsing_errors=True,
                                    max_iterations=5,
                                    early_stopping_method='generate',
                                    agent=agent,
                                    verbose=False
                                    )

    
    generated_response = agent_executor_instance.invoke({'query':query})
        
    tool_call_info = {}
    if generated_response.get('intermediate_steps'):  # Check if there are any intermediate steps
        tool_call_info['query'] = generated_response['query']
        tool_call_info['output'] = generated_response['output']
        tool_call_info['tool_call'] = "tool_call"
    else:
        tool_call_info = {'query': generated_response['query'], 'output': generated_response['output'], 'tool_call': 'no_tool_call'}
    

    print("-------------Agent Done---------------")
    print(".")
    print(".")
    print(".")
    yield generated_response
    print("Now doing the evaluation for agent trajectory.......")
    print(".")
    print(".")
    print(".")
    agent_eval_response = get_agent_evaluation(generated_response, llm = llm)
    print(".")
    print(".")
    print("trajectory Evaluation Finished.......")
    print(".")
    print(".")
    print(".")
    print("-------------Returning Value---------------")
    yield agent_eval_response
    
    
    

def generate_response_no_yield(query:str):
    
    prompt_agent = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                f"""
                You are a good assistant. """
            ),
            ("placeholder", "{chat_history}"),
            ("human", "{query}"),
            ("placeholder", "{agent_scratchpad}"),
        ],
    )
    senderId = "senderId"
    tools  = [leadTool, colorTool, greetingsTool]       
    agent = create_tool_calling_agent(llm, tools, prompt_agent)


    agent_executor = AgentExecutor(tools=tools,
                                    return_intermediate_steps=True,
                                    handle_parsing_errors=True,
                                    max_iterations=5,
                                    early_stopping_method='generate',
                                    agent=agent,
                                    verbose=False
                                    )

    
    generated_response = agent_executor.invoke({'query':query})
    
    

    output = generated_response.get('output')
    
    tool_call_info = {}
    if generated_response.get('intermediate_steps'):  # Check if there are any intermediate steps
        tool_call_info['query'] = generated_response['query']
        tool_call_info['output'] = generated_response['output']
        tool_call_info['tool_call'] = "tool_call"
    else:
        tool_call_info = {'query': generated_response['query'], 'output': generated_response['output'], 'tool_call': 'no_tool_call'}
    

    print("-------------Agent Done---------------")
    print(".")
    print(".")
    print(".")

    print("Now doing the evaluation for agent trajectory.......")
    print(".")
    print(".")
    print(".")
    agent_eval_response = get_agent_evaluation(generated_response, llm = llm)
    print(".")
    print(".")
    print("trajectory Evaluation Finished.......")
    print(".")
    print(".")
    print(".")
    print("-------------Returning Value---------------")
    return generated_response, agent_eval_response
    
    
    