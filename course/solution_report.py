# Løsningsforslag til rapport

# 1. Prompt Template
report_prompt = PromptTemplate.from_template("""
You are an expert HR and technical operations analyst. I will provide you with a dataset of employee feedback collected from an IT company.

Your task is to deeply analyze this feedback and generate a concise executive-level summary report in markdown format that includes:

1. Key Takeaways
Provide a short summary of the overall feedback in 3-5 bullet points. Focus only on the main issues or areas of satisfaction.
Include both positive and negative themes, but prioritize the most important and impactful points.
Limit each point to 1-2 sentences.
Before finalizing each point, take a moment to reflect on why each issue might be present (e.g., systemic problems, temporary issues, resource constraints, etc.)

2. Suggested Improvements
Based on the overall feedback, propose 2-3 high-level, actionable measures that the company could take to address the most pressing issues and enhance overall performance or satisfaction.
Each suggestion should be brief, directly tied to the feedback, and strategic in nature.
Think about short-term vs long-term solutions and consider the feasibility of each suggestion.

3. Output
Present your findings in a structured way with clear section headings, bullet points for easy scanning, and a consise, direct and professional tone suitable for leadership review.

This is the employee feedback data: {summary_text}
""")

# 2. Class for structured output
class ReportForLeadership(BaseModel):
    "Raport for the leadership of an IT-company on results of an internal IT-survey."
    snappy_title : str = Field(
        description="A fitting title for the report. Must begin with '# ' to ensure easy markdown formatting."
    )
    intro : str = Field(
        description="1 sentence describing thepurpose of the report." 
    )
    key_takeaways : str = Field(
        description="3-5 bulletpoints describing the key-takeaways. Limit each point to 1-2 sentences." 
    )
    suggested_improvements : str = Field(
        description="2-3 actionable measures for the company. Keep it brief."
    )
    outro: str = Field(
        description="1 sentence ending for the report. Be creative." 
    )

# 3. Report-chain
report_chain_structured_output = report_prompt | llm.with_structured_output(
    ReportForLeadership,
    method="json_schema",
    strict=True,
)

# 4. Create report 
report = report_chain_structured_output.invoke({"summary_text": summary.summary})

display(Markdown(
    "\n\n".join([report.snappy_title,
                 report.intro,
                 '## Key-takeaways',report.key_takeaways,
                 '## Suggested improvements',report.suggested_improvements,
                 report.outro])
                 
))