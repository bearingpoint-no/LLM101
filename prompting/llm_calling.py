from utils.llm import LLM
#from utils.dataset_c import FeedbackData
import pandas as pd

# Calling the LLM


def categorize(n):
    data = pd.read_csv('prompting/output_df_filtered.csv')

    data_subset = data.head(n)  # Example: Get the first n rows

    # Prompt
    task = f"""
Categorize the feedback in the dataframe {data_subset} by identifying the key themes or topics discussed in each row. 
Return one word per category that best captures the core focus of the feedback. 
Categories should reflect the most important aspects of the feedback, such as 'Health,' 'Technology,' 'Communication,' or others.
Additionally, provide a short sentence summarizing the overall sentiment of each feedback. 
The sentiment should account for both positive and negative elements, and include mixed or neutral sentiments when appropriate. 
Ensure to consider all sentences within each row, as the feedback may have multiple perspectives or contradictions that influence the sentiment and category.
For each row, carefully analyze the relationships between sentences, and resolve any conflicts or ambiguities in sentiment or category. 
The feedback may cover multiple topics or conflicting feelings—synthesize the information to provide a balanced and reasoned response.
    """

    # Giving the task to LLM
    response = LLM.llm.invoke(task).content

    # Return the response
    return response


print(categorize(10))
