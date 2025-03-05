from langchain_openai import AzureChatOpenAI
from dotenv import find_dotenv, load_dotenv
import os
#from utils.timer import timer

# Get environment variables
load_dotenv(find_dotenv(), override=True)

class Llm:
    # Connect to llm
    llm = AzureChatOpenAI(
        azure_deployment=os.environ["AZURE_OPENAI_DEPLOYMENT_GPT_4O_MINI"],
        model=os.environ.get("OPENAI_MODEL_GPT_4O-MINI", default="gpt-4o-mini"),
        temperature=0,
    )

LLM = Llm()


print(Llm.llm.invoke("whats up?").content)