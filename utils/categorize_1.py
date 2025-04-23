from pydantic import BaseModel, Field
from typing import Literal, Optional


class Categorize_search(BaseModel):
    """Categorization of IT-questionaire feedback."""

    fb: str = Field(description="Return just the feedback verbatim.")
    categories: Literal[
        "Technology",
        "IT support",
        "Network",
        "Other",
    ] = Field(
        description="Categorize the feedback into the most fitting category. If the categories provided are not a perfect fit, default to 'Other'."
    )
    if_other: str = Field(
        description="If you chose to categorize the feedback as 'Other', return an explanation as to why and what category you think would be the best fit for the feedback."
    )


class Categorize_bound(BaseModel):
    """Categorization of IT-questionaire feedback."""

    fb: str = Field(description="Return just the feedback verbatim.")
    categories: Literal[
        "Cyber security",
        "IT training",
        "IT support",
        "Quality of technology",
        "Data quality",
        "Network",
    ] = Field(description="Categorize the feedback into the most fitting category.")
    rating: Optional[int] = Field(
        description="Your certainty of the corectness of the best category on a scale from 1-10"
    )
    reason: str = Field(
        description="Give a short scentence as to why you think this category is the best fit."
    )


class Categorize_think(BaseModel):
    """Categorization of IT-questionaire feedback."""

    cot: str = Field(
        description="Think about and explain why this category is the most fitting one and why you chose it."
    )
    categories: Literal[
        "Cyber secyrity", "IT training", "IT support", "Technology quality"
    ] = Field(description="Categorize the feedback into the most fitting category.")


class Categorize(BaseModel):
    "Categorization of feedback on IT-services."

    # Thoughts: Forklar tankegangen din.
    fb: str = Field(description="Return just the feedback verbatim.")
    cat_1: str = Field(description="The best fitting general category")
    rating: Optional[int] = Field(
        description="Your certainty of the corectness of the best category on a scale from 1-10"
    )


class Enrich(BaseModel):
    "Enrichment of dataset to make it more human"

    cat_1: str = Field(
        description="Return the enriched dataset in a comma separated format like the format of the input dataset"
    )


class Sentiment(BaseModel):
    "Provide a sentiment analysis of feedback"

    fb: str = Field(description="Return just the feedback verbatim.")
    sentiment: str = Field(
        description="Return the sentiment analysis of the feedback as a label. Either positive, negative or mixed."
    )
    depth_sent: str = Field(
        description="Return a more nuanced analysis of the sentiment. Is there more complexity to the sentiment than just positive or negative?"
    )

    feeling: str = Field(
        description="What feelings are most predominant in the sentiment of the feedback? Return just the feeling(s)."
    )
