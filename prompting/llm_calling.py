from utils.llm import LLM
from utils.dataset_c import FeedbackData
import pandas as pd

# Calling the LLM


def categorize(n):
    data = FeedbackData.df

    data_subset = data.head(n)  # Example: Get the first n rows

    # Prompt
    task = f"""
    Categorize the feedback in the dataframe {data_subset} reflecting the main takeaways. 
    """

    # Giving the task to LLM
    response = LLM.llm.invoke(task).content

    # Return the response
    return response


print(categorize(10))
