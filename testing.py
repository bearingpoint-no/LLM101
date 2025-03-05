import kagglehub
import pandas as pd
from kagglehub import KaggleDatasetAdapter
 
'''
This file consists of 7600 testing samples of news articles that contain 3 columns.
The first column is Class Id, the second column is Title and the third column is Description.
The class ids are numbered 1-4 where 1 represents World, 2 represents Sports,
3 represents Business and 4 represents Sci/Tech.
'''
 
class News_dataset:
 
    # Load a DataFrame with a specific version of a CSV
    df = kagglehub.load_dataset(
        KaggleDatasetAdapter.PANDAS,
        "amananandrai/ag-news-classification-dataset",
        "test.csv",
    )
 
    titles = df['Title']
   
    descriptions = df['Description']