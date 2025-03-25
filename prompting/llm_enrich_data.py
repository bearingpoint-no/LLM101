from utils.llm import LLM
from utils.dataset_c import FeedbackData
import pandas as pd
from utils.categorize_1 import Categorize

# Calling the LLM

    # Prompt
task = f"""
I have made a fake dataset containing feedback from employees at a company conserning their IT services.
I want to use this dataset in a demo to highlight the differences between th 04-mini model 
(without reasoning, but with structured output) and the 03-mini (with reasoning and with structured output). 
Can you enrich my dataset? Make the feedback more multi-faceted and make sure more subtle feelings like 
frustration, confusion and joys (just examples, please add on as you wish) are present in the feedback? 
Just make sure the dataset will ensure a different quality of response from the two models.
"""
structured_llm = LLM.llm_res.with_structured_output(Categorize)

response = structured_llm.invoke(task + f"\n'{pd.read_excel('./shuffled_df_LLM101.xlsx')}'")

# Giving the task to LLM
print(response)

with open('./output_df.txt','w') as ofile:
    ofile.write(response.cat_1)

