from langchain.tools import Tool,StructuredTool
import os
import pprint
from dotenv import load_dotenv, find_dotenv
from langchain.tools import Tool,StructuredTool
from langchain.schema.runnable import RunnableMap
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.output_parsers.json import JsonOutputParser
from langchain.agents import create_tool_calling_agent, AgentExecutor
string_parser= StrOutputParser()
json_parser = JsonOutputParser()
from langchain_groq import ChatGroq
from Agent.Schema import docs, QueryInput # The context to be used for color prompt
from eval_it import chain_evaluate_output
from Agent.model import llm
load_dotenv(find_dotenv())

def offer_tool(query: str):
    """
Executes a tool to respond to queries related to offers, using a predefined context.
The function processes the query through a series of transformations and evaluations,
including a language model and a string parser, to generate a response. It also evaluates
the quality of the response using a context evaluation function.

Args:
    query (str): The user query to be processed.

Returns:
    str: The response generated based on the query and context.
"""
    context = docs
    print("====Color Tool====")
    print(f"------------{query}---------")
    color_prompt =ChatPromptTemplate.from_template( """ You are given a context that contains the color no matter what the query is, Answer the query based on the context provided to you.  
    Do not answer anything which is not present in the context. 
    ##query:`{query}`
    ##context: {context}
    Be concise with your response, just answer what is asked in the query, be conversational as much as possible.
    """)
    chain = RunnableMap({
        'query': lambda x: x['query'],
        'context': lambda x: context
    }) | color_prompt | llm | string_parser
    res = chain.invoke({"query": query})
    
    evaluation_explanation, evaluation_score = chain_evaluate_output(query=query, retrieval_context= context, llm_output=res)
    print("\n\n----------------------Chain Evaluation------\n\n")
    print("Evaluation Explanation ->",evaluation_explanation ,"\n\nEvaluation Score->", evaluation_score)
    print("\n--------------------------------------------")
    return res

def greetings_tool(query: str):
    """
Processes a greeting query using a language model and evaluates the response.

This function takes a greeting query, processes it through a language model
pipeline, and evaluates the output. It prints the evaluation results and 
returns the processed response.

Args:
    query (str): The greeting query to be processed.

Returns:
    str: The processed response from the language model.
"""
    print("====Greetings Tool====")
    print(f"------------{query}---------")
    color_prompt =ChatPromptTemplate.from_template(""" You are a good virtual assistant. Handle the greetings properly in a polite manner.
    ##query:\n{query}\n\n\n
    # """)
    chain = RunnableMap({
        'query': lambda x: x['query'],
    }) | color_prompt | llm | string_parser
    res = chain.invoke({"query": query})
    chain_eval = chain_evaluate_output(query=query, retrieval_context= [], llm_output=res)
    print(chain_eval)
    return res
def lead_capture(query: str):
    """
Capture a lead based on the provided query.

Parameters:
    query (str): The query string used to capture the lead.

Returns:
    str: Confirmation message indicating successful lead capture.
"""
    return "The Lead Has been captured Sucessfully."


colorTool = StructuredTool.from_function(
            name='offerTool',
            func=offer_tool,
            description="A tool that responds to query related to offers in chrismas, new year and so on.",
            args_schema=QueryInput,
            return_direct=True
        )
greetingsTool = StructuredTool.from_function(
            name='greetingsTool',
            func=greetings_tool,
            description="A tool that handles every greetings",
            args_schema=QueryInput,
            return_direct=True
        )
leadTool = StructuredTool.from_function(
            name='leadTool',
            func=lead_capture,
            description="A tool that responds to query related capturing the lead.",
            args_schema=QueryInput,
            return_direct=True
)

