from utils.llm import Llm
from utils.dataset_c import News_dataset

# Prompting example 3: First, we ask the llm to find the four main categories based on the descriptions
## The descriptions are provided as a list of strings
# Load descriptions
descriptions = News_dataset.descriptions.tolist()

# Limit the number of descriptions for category identification
descriptions_subset = descriptions[:5]  # Adjust the number based on your needs

# Step 1: Ask LLM to determine the 4 main categories based on the descriptions
task_3_0 = f"""
Here are several article descriptions from a dataset:

1. {descriptions_subset[0]}
2. {descriptions_subset[1]}
3. {descriptions_subset[2]}
4. {descriptions_subset[3]}
5. {descriptions_subset[4]}

Determine the four main one-word categories that best represent the articles. 
These categories should be distinct and cover the major topics found across all the descriptions. 
Examples could include "Politics", "Technology", "Health", etc., but make sure to derive them based on the actual content of these descriptions.
The output should only contain four words separated by commas, nothing more!
"""
# Get the categories from the LLM
categories = Llm.llm.invoke(task_3_0)

# Save the categories to a txt file in the desired format
with open("cat.txt", "w") as cat_file:
    # Write categories, assuming categories is a string
    cat_file.write(f"Categories:\n{categories}\n")

# Step 2: Read categories from 'cat.txt' and use it to categorize articles
with open("cat.txt", "r") as cat_file:
    categories_from_file = cat_file.read()

# Step 3: Categorize each article description based on the identified categories
task_3_1 = f"""
Here are the 4 categories identified based on all article descriptions:
{categories_from_file}

Now, please categorize each of the following article descriptions by assigning them to one of the four categories listed above.

Article descriptions:
1. {descriptions[0]}
2. {descriptions[1]}
3. {descriptions[2]}
4. {descriptions[3]}
5. {descriptions[4]}

For each article, provide only the name of the category (one word) that best fits its content. 
"""

# Get the final output from the LLM
final_output = Llm.llm.invoke(task_3_1)

# Save the final output to 'prompt_3.txt'
with open("prompt_3.txt", "w") as output_file:
    output_file.write("Article Categorization:\n")

# Print or process the final output if needed
print(final_output)