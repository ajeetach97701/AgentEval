# Agent Evaluation and Tooling Framework

This project provides a structured framework for building and evaluating AI agents using LangChain and Groq models. It includes tools for handling queries related to offers, greetings, and lead capturing, along with an evaluation module for assessing response accuracy based on retrieved context.

## Features
- **Agent Tools:** Predefined tools for responding to offer-related queries, greetings, and lead capturing.
- **Evaluation Module:** Assess the quality of LLM responses against retrieved context.
- **LangChain Integration:** Uses LangChain's tool framework and evaluation chains.
- **Support for Groq LLMs:** Uses Groq-based models for inference and evaluation.

## Installation
Ensure you have Python installed. Then, install the dependencies using:
```sh
pip install -r requirements.py
```

## Environment Variables
Create a `.env` file and add the necessary API keys:
```
GROQ_API=<your-groq-api-key>
```

## Future Enhancements
- **More tools** for different agent functionalities.
- **Fine-tuning evaluation criteria** to improve accuracy.
- **Additional LLM support** beyond Groq models.


## Project Structure
```
├── Agent
│   ├── model.py         # Defines the LLM used for inference
│   ├── Schema.py        # Contains structured query input/output schemas
│   ├── Tools.py         # Defines the agent's tools (offer handling, greetings, lead capture)
├── eval_it.py           # Evaluation functions for assessing LLM response quality
├── requirements.py      # List of dependencies
├── .env                 # Environment variables (e.g., API keys)
└── README.md            # Project documentation
```


## Running the Project
To start the project, execute the `main.py` file:

```bash
python main.py
```

### Usage
1. The program will prompt you to enter a query.
2. Enter your query, and the agent will generate a response.
3. The system will evaluate the response and provide a score along with reasoning.
4. Type `exit` to terminate the program.

### Example Output
```
Enter your query below (or type 'exit' to quit):
>> Query: Chrismas Offer
====Color Tool====

----------------------Chain Evaluation------


Evaluation Explanation -> The user asked about a Christmas Offer, but the context provided only contains information about a New Year Offer. The result accurately reflects this by stating that there is no information about a Christmas Offer. The result is correct based on the context. 

Evaluation Score-> 1

-------------Agent Processing Done----------
--------------------------------------------

Response: Based on the context provided, there is no information about a Christmas Offer. The only offer mentioned is the New Year Offer, which includes a Monthly Membership (Auto-renewable) for 235 SAR, a 3-Month Membership for 525 SAR, a 6-Month Membership for 1230 SAR, and a 12-Month Membership for 1960 SAR.
--------------------------------------------

Now doing the evaluation for agent trajectory.......
.
.
trajectory Evaluation Finished.......
.
.
.
-------------Returning Evaluation Result---------------
Agent Eval Score: 1.0
Reason for the score is: The final answer is helpful because it provides information about the New Year Offer. The model uses a logical sequence of tools to answer the question. The model uses the tool in a helpful way. The model does not use too many steps to answer the question. The model uses the appropriate tool to answer the question.

Judgment: The model gets a score of 5.
```

## Contributions
Feel free to open issues or submit pull requests for improvements!

## License
This project is licensed under the MIT License.

## Contact

For support and queries, contact: ajeetacharya02@gmail.com