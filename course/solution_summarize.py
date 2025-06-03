# Løsningsforslag til oppsummering 

# 1. Prompt Template
summary_prompt = PromptTemplate.from_template("""
You are a domain expert in internal IT operations and organizational analysis. You will be provided with a dataset containing qualitative feedback from employees in an IT company. 
Each row in the dataset represents a feedback entry and is associated with a specific category.

For each category, carefully:
1. Read and interpret the feedback entries assigned to that category.
2. Identify core themes, recurring patterns, and contrasting opinions within that category.
3. Evaluate the feedback logically: What are the likely underlying causes of recurring issues or praises? Are there signs of systemic problems, isolated incidents, or misaligned expectations?
4. Summarize each category in 3 to 6 bullet points, highlighting key sentiments (positive and negative), representative concerns or compliments, and any significant outliers

Present your findings in a clean, professional way with one section per category. 

This is the employee feedback data: {survey_results}
""")

# 2. Class for structured output
class SummarizeFeedback(BaseModel):
    "Summary of the different categorizes recognized in the feedback from an IT-survey."
    summary : str = Field(
        description="For each category: Category name and 3-6 bullet points summarizing the category."
    )

# 3. Summary-chain
summary_chain_structured_output = summary_prompt | llm.with_structured_output(
    SummarizeFeedback,
    method="json_schema",
    strict=True,
)

# 4: Call the model with the dataset from the survey
summary = summary_chain_structured_output.invoke({"survey_results": df})

# A nice way to show the output from the model
display(Markdown(summary.summary))

