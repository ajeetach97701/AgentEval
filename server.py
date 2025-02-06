from fastapi import FastAPI, HTTPException

from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import time
from Agent.agent import generate_response

app = FastAPI()

class QueryRequest(BaseModel):
    query: str
    senderId: str




@app.get("/", response_class=HTMLResponse)
async def home():
   with open("template.html", "r") as file:
    content = file.read()
   return HTMLResponse(content=content)


class QueryResponse(BaseModel):
    query: str
    response: str
    agent_eval_score: float
    reasoning: str
    duration: float


@app.post("/query", response_model=QueryResponse)
async def handle_query(request: QueryRequest):
    """
Handles POST requests to the '/query' endpoint, processing the input data
and returning a response conforming to the QueryResponse model.

Args:
    query (str): The input query string.
    response (str): The generated response from the agent.
    agent_eval_score (float): The evaluation score assigned to the response by the agent.
    reasoning (str): The reasoning or explanation behind the response.
    duration (float): The time taken to generate the response, in seconds.

"""
    start_time = time.time()

    if request.query.lower() == 'exit':
        raise HTTPException(status_code=400, detail="The 'exit' command is not allowed in this context.")

    try:
        generate_response_instance = generate_response(query=request.query)
        generated_response = next(generate_response_instance)
        
        # Generate agent evaluation
        agent_eval_response = next(generate_response_instance)

        end_time = time.time()
        duration = end_time - start_time

        return QueryResponse(
            query=generated_response['query'],
            response=generated_response['output'],
            agent_eval_score=agent_eval_response['score'],
            reasoning=agent_eval_response['reasoning'],
            duration=duration
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
