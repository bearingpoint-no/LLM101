from utils.llm import LLM
#from utils.dataset_c import FeedbackData
import pandas as pd

# Calling the LLM


def categorize(n):
    data = pd.read_csv('prompting/output_df_filtered.csv')

    data_subset = data.head(n)  # Example: Get the first n rows

    # Prompt
    task = f"""
    Categorize the feedback in the dataframe {data_subset} reflecting the main takeaways. 
    Return one word per category. Examples could be "Health" or "Technology". 
    Additionally, give me a short sentence per feedback describing the sentiment of the text, so I can see if the feedback is positive or negative. 
    """

    # Giving the task to LLM
    response = LLM.llm.invoke(task).content

    # Return the response
    return response


print(categorize(10))
