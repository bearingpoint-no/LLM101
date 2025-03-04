from utils.llm import Llm
from utils.categorize_1 import Categorize, Categorize_bound
from utils.dataset_c import News_dataset
'''
structured_llm = Llm.llm.with_structured_output(Categorize)
for i in range(0,10):
    response = structured_llm.invoke(f"Categorize this news article: '{News_dataset.descriptions[i]}'")

    print(response, News_dataset.descriptions[i])
'''

structured_llm = Llm.llm.with_structured_output(Categorize_bound)
task = '''Categorize the folowing news article into the best fitting category. Allowed categories:\n
          1 - World\n
          2 - Sports\n
          3 - Business\n
          4 - Sci/Tech\n\n
        '''
for i in range(0,10):
    response = structured_llm.invoke(task + f"Article:\n'{News_dataset.descriptions[i]}'")
    print(response, f'label = {News_dataset.labels[i]}')
