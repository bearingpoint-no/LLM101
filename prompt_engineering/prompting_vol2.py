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


# Example 2: More, less complex tasks
def categorize(d: str):
    # Step 1: Identify key themes
    task_1 = f"""
    Please analyze the following descriptions of articles and identify key themes or topics within the content. 
    Do not categorize yet. 
    Just focus on extracting the main ideas or concepts. If the feedback includes multiple themes, list the main one.

    Descriptions:
    {News_dataset.descriptions}
    """
    identified_themes = Llm.llm.invoke(task_1)  # Get the themes

    # Step 2: Suggest categories based on identified themes
    task_2 = f"""
    Based on the following key themes, categorize them into one of exactly four categories. 
    Each category should be one word and directly related to the themes in the description. 
    If no category fits, suggest 'Other'. 
    Ensure that the categories are distinct and logically related to the key themes.

    Key Themes:
    {identified_themes}

    Suggested Categories:
    """
    suggested_categories = Llm.llm.invoke(task_2)  # Get the suggested categories

    # Step 3: Verify and refine the suggested categories
    task_3 = f"""
    Please review the following suggested categories and ensure they are distinct and relevant to the feedback. 
    If any category seems too vague or irrelevant, refine it. 
    If all the categories are appropriate, confirm them.

    Suggested Categories:
    {suggested_categories}

    Final Categories:
    """
    final_categories = Llm.llm.invoke(task_3)  # Get the final categories

# Open a file in write mode to store the output
with open('prompt_2.txt', 'w') as file:
    # Loop over the descriptions in the News_dataset
    num_descriptions = len(News_dataset.descriptions)
    for i in range(num_descriptions):
        # Get the final categories for each description
        final_categories = categorize(News_dataset.descriptions[i])

        # Write the output (only the categories) to the file, one category per line
        file.write(f"Article {i+1}: {final_categories}\n")  # Write article and its categories in a clean format

# When finished, print the total number of descriptions processed
print(f"Finished processing {num_descriptions} descriptions. Results saved to 'prompt_2.txt'.")

