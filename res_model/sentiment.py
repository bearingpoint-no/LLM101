import pandas as pd

from utils.dataset_c import FeedbackData
from utils.llm import LlmRes, Llm
from utils.categorize_1 import Sentiment


def sentiment_analysis(data, llm_model):
    # Prompt
    task = f"""
    Provide a sentiment analysis of the following feedback: {data}.
    """

    # Giving the task to LLM
    structured_llm = llm_model.with_structured_output(
        Sentiment, method="function_calling"
    )

    response = structured_llm.invoke(task)

    # Return the response
    return response


responses_3O = {}
responses_4O = {}

for i in range(10):
    responses_3O[str(i)] = sentiment_analysis(
        FeedbackData.df["Feedback"][i], LlmRes.llm
    )
    responses_4O[str(i)] = sentiment_analysis(FeedbackData.df["Feedback"][i], Llm.llm)
    print(f"\n-----Feedback-----\n {responses_3O[str(i)].fb}\n")
    print(
        f"-----Sentiment-----\n 4O: {responses_4O[str(i)].sentiment}\n 3O: {responses_3O[str(i)].sentiment}\n"
    )
    print(
        f"-----Feelings-----\n 4O: {responses_4O[str(i)].feeling}\n 3O: {responses_3O[str(i)].feeling}\n"
    )
    print(
        f"-----In-depth analysis-----\n 4O: {responses_4O[str(i)].depth_sent}\n 3O: {responses_3O[str(i)].depth_sent}\n\n"
    )
