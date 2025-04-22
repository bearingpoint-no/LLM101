from langchain_openai import AzureChatOpenAI
from dotenv import find_dotenv, load_dotenv
import os


# Get environment variables
load_dotenv(find_dotenv(), override=True)


class Llm:
    """
    Class containing the language model.
    """

    llm = AzureChatOpenAI(
        azure_deployment=os.environ["AZURE_OPENAI_DEPLOYMENT_GPT_4O_MINI"],
        model=os.environ.get("OPENAI_MODEL_GPT_4O_MINI", default="gpt-4o-mini"),
        openai_api_key=os.environ["OPENAI_API_KEY_4O"],
        openai_api_version=os.environ["OPENAI_API_VERSION_4O"],
        azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT_4O"],
        temperature=0,
    )


class LlmRes:
    """
    Class containing the language model.
    """

    llm = AzureChatOpenAI(
        azure_deployment=os.environ["AZURE_OPENAI_DEPLOYMENT_GPT_3O_MINI"],
        model=os.environ.get("OPENAI_MODEL_GPT_3O_MINI", default="o3-mini"),
        openai_api_key=os.environ["OPENAI_API_KEY_3O"],
        openai_api_version=os.environ["OPENAI_API_VERSION_3O"],
        azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT_3O"],
        reasoning_effort="high",
        # reasoning_effort: str,
        # Constrains effort on reasoning for reasoning models.
        # Reasoning models only, like OpenAI o1 and o3-mini.
        # Currently supported values are low, medium, and high.
        # Reducing reasoning effort can result in faster responses and fewer tokens used on reasoning in a response.
    )


# LLM = Llm()

# print(Llm.llm.invoke("whats up?").content)
