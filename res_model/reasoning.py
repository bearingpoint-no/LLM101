import pandas as pd

from utils.dataset_c import FeedbackData
from utils.llm import LlmRes, LLM
from utils.categorize_1 import Sentiment

# Calling the LLM


def categorize(n):
    data = FeedbackData.df

    data_subset = data.head(n)  # Example: Get the first n rows

    # Prompt
    task = f"""
    Categorize the feedback in the dataframe {data_subset} reflecting the main takeaways. 
    """

    # Giving the task to LLM
    response = LlmRes.llm.invoke(task).content

    # Return the response
    return response


# print(categorize(10))


def sentiment_analysis(n, llm_model):
    data = FeedbackData.df["Feedback"].head(n)

    # Prompt
    task = f"""
    Categorize the feedback in the dataframe {data} reflecting the main takeaways. 
    """

    # Giving the task to LLM
    structured_llm = llm_model.with_structured_output(Sentiment)

    response = structured_llm.invoke(task)

    # Return the response
    return response


print(sentiment_analysis(10, LlmRes.llm))
# print(sentiment_analysis(10, LLM.llm))
