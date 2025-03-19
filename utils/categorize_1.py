from pydantic import BaseModel, Field
from typing import Optional


class Categorize(BaseModel):
    """Categorization of news article."""
    #Thoughts: Forklar tankegangen din.
    cat_1: str = Field(description="The best fitting genral category")
    cat_2: str = Field(description="The second to best fitting general category")
    rating: Optional[int] = Field(
        description="Your certainty of the corectness of the best category on a scale from 1-10"
    )


class Categorize_bound(BaseModel):
    """Categorization of news article into a predetermined set of categories."""

    category: int = Field(
        description="The number corresponding to the best fitting category."
    )
    certainty: float = Field(
        description="Certainty of correctness in categorizing (0-1 scale)."
    )

