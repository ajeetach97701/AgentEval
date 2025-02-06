from typing import List
from langchain.evaluation import load_evaluator, ContextQAEvalChain
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
import os
from dotenv import load_dotenv
load_dotenv()
groq_api_key = os.getenv("GROQ_API")
import json


def chain_evaluate_output(query: str, retrieval_context: List, llm_output: str):
    """Evaluates the output of a language model (LLM) against a given query and retrieval context.
    This function uses a prompt template to assess whether the LLM's prediction is accurate
    based on the provided context. It returns a detailed explanation and a score indicating
    the quality of the prediction.
    
    Args:
    
    query (str): The user query to be evaluated.
    retrieval_context (List): The context data retrieved from a vector store.
    llm_output (str): The prediction made by the LLM for the given query.
    
    Returns:
    tuple: A tuple containing the evaluation explanation (str) and the evaluation score (float).
"""
    prediction = [{"result": llm_output}]
    examples = [
        {
            "query": query,
            "context": retrieval_context,
            "result": prediction
        }
    ]
    prompt_template = PromptTemplate.from_template(
        """You are given the three parameters that you have to analyze, 
        input: Description(content = "This is the user input in which the user asks query."),
        result: Desctiption(content = "This is the result or the prediction made by llm of the user query by analyzing the context(RAG)"),
        context: Description(content = "This is the data retrieved from the vector store on which the RAG is performed.")
        Evaluate the input, the context and the result to see if the result produced by the llm is correct or not based on the context. 
        You have to provide a json output having the following keys:
        Dict(
            explanation: "Explain the evaluation in string format in detail",
            score: "the score on the scale from 0 to 1(Floating point numbers) bad result is 0, best is 1 and average is 0.5.
            )
            Reason step by step and finally, provide a json object without any prefixes like- JSON, DICT etc
            DATA
            ----
            input: {query}
            result: {result}
            context: {context}
            ---
            give the response in only json without any other text outside of the json
            """
            )
    llm = ChatGroq(api_key=groq_api_key,
                   model="mixtral-8x7b-32768",
                   temperature=0,
                   max_tokens=None,
                   timeout=None,
                   max_retries=2
                   )
    context_eval = ContextQAEvalChain(prompt=prompt_template, llm=llm)
    
    eval_result = context_eval.evaluate(examples=examples, predictions=prediction)[0]['text']
    eval_result_json  = json.loads(eval_result)
    evaluation_explanation =eval_result_json['explanation']
    evaluation_score = eval_result_json['score']
    return evaluation_explanation, evaluation_score
    
    
# query = "What is price of grand i10?"
# llm_output = "The Grand i10 price is not available"
# retrieval_context = ["price of SANTA FE: 'Santa FeGLS 4WD AT': '18,996,000'",
#  "price of PALISADE:[{'PALISADE GLS 4WD AT Diesel': '23,596,000'}]", 
#  "price of KONA:[{'KONA GL Electric': '5,996,000'}, {'KONA GLS Electric': '6,496,000'}]",
#  "price of IONIQ 5:[{'IONIQ 5 GLS VISION ROOF 100 kW': '92,96,000'}, {'IONIQ 5 GLS VISION ROOF 124.9 kW': '1,03,96,000'}]",
#  "price of i20:[{'i20 Magna': '3,996,000'}, {'i20 Sportz': '4,396,000'}]",
#  "price of grand_i10:[{'i10 Sportz 2023': '3,896,000'}, {'i10 Magna AMT 2023': '3,956,000'}, {'i10 Era 2024': '3,256,000'}, {'i10 Magna 2024': '3,796,000'}, {'i10 Sportz 2024': '3,996,000'}, {'i10 Magna AMT 2024': '4,056,000'}]",
#  "price of CRETA:[{'CRETA E 2023': '5,456,000'}, {'CRETA S 2023': '6,256,000'}, {'CRETA S+ 2023': '6,596,000'}, {'CRETA SX 2023': '7,056,000'}, {'CRETA E 2023 Diesel': '5,156,000'}, {'CRETA SX CVT 2023': '7,696,000'}]", 
#  "price of ALL NEW CRETA:[{'All New Creta E': '5,696,000'}, {'All New Creta S(O) MT': '6,896,000'}, {'All New Creta SX': '7,296,000'}, {'All New Creta S(O) CVT': '7,496,000'}, {'All New Creta SX Tech MT': '7,556,000'}, {'All New Creta SX Tech CVT': '8,196,000'}, {'All New Creta SX(O)': '8,696,000'}]", 
#  "price of TUCSON:[{'Tucson GL 2WD MT': '10,796,000'}, {'Tucson GLX 2WD AT': '13,796,000'}, {'Tucson GLX+ 2WD AT': '14,496,000'}, {'Tucson GLX 4WD AT Diesel': '16,096,000'}, {'Tucson GLX 4WD AT TURBO': '16,296,000'}]",
#  "price of EXTER:[{'Exter EX 2024': '3,596,000'}, {'Exter S 2024': '4,196,000'}, {'Exter SX 2024': '4,596,000'}]",
#  "price of STARIA AMBULANCE:[{'STARIA Standard Trim Ambulance': 'For price details please call 9801969627/9801201017'}, {'STARIA High Trim Ambulance': 'For price details please call 9801969627/9801201017'}]", 
#  "price of VENUE F/L: 'Venue E 1.2 2024': '4,096,000', 'Venue S 1.2 2024': '4,496,000', 'Venue SX 1.2 2024': '5,356,000', 'Venue S(O) DCT 2024': '5,896,000'"
#  ]
# explanation, score = chain_evaluate_output(query=query, retrieval_context=retrieval_context, llm_output=llm_output)

# print(f"-------------------------\n\n query: {query}\n\n llm_output: {llm_output}\n\n Explanation: {explanation}\n\n Score:{score}\n-------------------------")

from typing import TypedDict, List

# Define the type for the dictionary
class AgentOutput(TypedDict):
    query: str
    output: str
    intermediate_steps: List[str]
    
    
def get_agent_evaluation(output:AgentOutput, llm:ChatGroq):
    evaluator = load_evaluator("trajectory", llm = llm)
    evaluation_result = evaluator.evaluate_agent_trajectory(
        prediction=output['output'],
        input=output['query'],
        agent_trajectory=output["intermediate_steps"],
        )
    return evaluation_result