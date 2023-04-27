import os
from langchain.tools import OpenAPISpec, APIOperation
from langchain.chains import OpenAPIEndpointChain
from langchain.requests import Requests
from langchain.llms import OpenAI

from dotenv import load_dotenv

load_dotenv()

spec = OpenAPISpec.from_file("mc_api.yaml")
# print(spec)

operation = APIOperation.from_openapi_spec(spec, '/publicなAPI/endpoint/', "get")

openai_api_key = os.getenv("OPENAI_API_KEY")
llm = OpenAI(openai_api_key=openai_api_key)

chain = OpenAPIEndpointChain.from_api_operation(
    operation,
    llm,
    requests=Requests(),
    verbose=True,
    return_intermediate_steps=True # Return request and response text
)
output = chain("attributesの種類を網羅的に教えてください")