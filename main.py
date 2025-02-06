
from Agent.agent import generate_response, generate_response_no_yield

import time


def call_yield():
    while True:

        query = input("Enter your query below (or type 'exit' to quit):\n>> ")
        start_time = time.time()

        if query.lower() == 'exit':
            print("Exiting the program...")
            break

        generate_response_instance = generate_response(query=query)
        generated_response = next(generate_response_instance)
        print(generated_response)
        print("\n\nQuery:", generated_response['query'])
        print("\n\nResponse:", generated_response['output'])
        
        
        agent_eval_response = next(generate_response_instance)
        
        print("\n\nAgent Eval Score:", agent_eval_response['score'])
        print("\n\nReason for the score is:", agent_eval_response['reasoning'])
        end_time = time.time()
        duration = end_time - start_time
        print(f"Time taken to run the function: {duration} seconds")


if __name__ == "__main__":
    call_yield()
    # call_no_yield()



