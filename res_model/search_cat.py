import pandas as pd

from utils.dataset_c import FeedbackData
from utils.llm import LlmRes, Llm
from utils.categorize_1 import Categorize_search


def categorize_feedback(data, llm_model):
    # Prompt
    task = f"""
    The following feedback is from an internal survey at 'IT and Things Company' where they asked their employees for feedback on their IT-services in general.
    Catgorize the feedback: {data}.
    """

    # Giving the task to LLM
    structured_llm = llm_model.with_structured_output(
        Categorize_search  # , method="function_calling"
    )

    response = structured_llm.invoke(task)

    # Return the response
    return response


responses_3O = {}
responses_4O = {}

for i in range(10):
    responses_3O[i] = categorize_feedback(FeedbackData.df["Feedback"][i], LlmRes.llm)
    responses_4O[i] = categorize_feedback(FeedbackData.df["Feedback"][i], Llm.llm)
    print(f"\n-----Feedback-----\n {responses_3O[i].fb}\n")
    print(
        f"-----Category-----\n 4O: {responses_4O[i].categories}\n 3O: {responses_3O[i].categories}\n"
    )
    print(
        f"-----If other-----\n 4O: {responses_4O[i].if_other}\n 3O: {responses_3O[i].if_other}\n"
    )
