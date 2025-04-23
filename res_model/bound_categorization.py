# Bound categorization

import pandas as pd

from utils.dataset_c import FeedbackData
from utils.llm import LlmRes, Llm
from utils.categorize_1 import Categorize_bound


def categorize_feedback(data, llm_model):
    # Prompt
    task = f"""
    The following feedback is from an internal survey at 'IT and Things Company' where they asked their employees for feedback on their IT-services in general.
    Catgorize the feedback: {data}.
    """

    # Giving the task to LLM
    structured_llm = llm_model.with_structured_output(
        Categorize_bound, method="function_calling"
    )

    response = structured_llm.invoke(task)

    # Return the response
    return response


responses_3O = {}
responses_4O = {}

for i in range(10):
    responses_3O[str(i)] = categorize_feedback(
        FeedbackData.df["Feedback"][i], LlmRes.llm
    )
    responses_4O[str(i)] = categorize_feedback(FeedbackData.df["Feedback"][i], Llm.llm)
    print(f"\n-----Feedback-----\n {responses_3O[str(i)].fb}\n")
    print(
        f"-----Category-----\n 4O: {responses_4O[str(i)].categories}\n 3O: {responses_3O[str(i)].categories}\n"
    )
    print(
        f"-----Rating of certainty-----\n 4O: {responses_4O[str(i)].rating}\n 3O: {responses_3O[str(i)].rating}\n"
    )
    print(
        f"-----Reason-----\n 4O: {responses_4O[str(i)].reason}\n 3O: {responses_3O[str(i)].reason}\n\n"
    )
