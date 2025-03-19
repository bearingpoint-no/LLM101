# Prompt engineering basics

'''
Poeng 1: Send mange, korte instrukser heller enn en større, komplisert instruks (iterer)
Poeng 2: Vær tydelig og presis
Poeng 3: Gi tilstrekkelig med kontekst
Poeng 3: Ha god struktur, bruk oppdelere for å markere skiller osv
Poeng 4: Gjør det umulig å misforstå. Tenk at du skal forklare oppgaven til et barn. Ikke still åpne spørsmål etc.
'''

from utils.llm import Llm
from utils.dataset_c import News_dataset


# Example 1: One big prompt
def categorize(d: str):
    # Prompt where the LLM is tasked with categorizing based on the article descriptions
    task = f"""Categorize the following descriptions into four relevant categories. 
    The categories should reflect key themes or topics in the articles. 
    If none of the categories fit, categorize as 'Other'. 
    You are allowed to choose multiple categories if they overlap, but make sure the categories are logical 
    and related to the content of the feedback. 
    Please identify categories based on the content provided, and avoid being too vague or general. 
    If unsure, select 'Other'.\n\n

    {d}\n

    Instructions:
    - Identify 4 categories from the feedback.
    - Categories should reflect distinct themes or topics.
    - If no category fits, use 'Other'.
    - You may select multiple categories if needed.
    - Ensure categories are logical, clear, and relevant to the feedback content."""
    
    # Invoking the model
    response = Llm.llm.invoke(task)  
    return response

# Open a file in write mode to store the output
with open('prompt_1.txt', 'w') as file:
    # Loop over the descriptions in the News_dataset
    num_descriptions = len(News_dataset.descriptions)
    for i in range(num_descriptions):
        kall_1 = categorize(News_dataset.descriptions[i])
        file.write(f"Output for Description {i+1}:\n{kall_1}\n\n")  # Writing the output to the file

# When finished, print the total number of descriptions processed
print(f"Finished processing {num_descriptions} descriptions. Results saved to 'prompt_1.txt'.")