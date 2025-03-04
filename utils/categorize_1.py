from pydantic import BaseModel, Field
from typing import Optional

class Categorize(BaseModel):
    '''Categorization of news article.'''

    cat_1: str = Field(description="The best fitting geenral category")
    cat_2: str = Field(description="The second to best fitting general category")
    rating: Optional[int] = Field(description="Your certainty of the corectness of the best category on a scale from 1-10")

class Categorize_bound(BaseModel):
    ''' Categorization of news article into an allowed predetermined set of categories.'''

    category: int = Field(description='The number corresponding to the best fitting category.')
    certainty: float = Field(description='Ceratinty of correctness in categorizing (0-1 scale).') 

