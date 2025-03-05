# Prompt engineering basics

'''
Poeng 1: Send mange, korte instrukser heller enn en større, komplisert instruks (iterer)
Poeng 2: Vær tydelig og presis
Poeng 3: Gi tilstrekkelig med kontekst
Poeng 3: Ha god struktur, bruk oppdelere for å markere skiller osv
Poeng 4: Gjør det umulig å misforstå. Tenk at du skal forklare oppgaven til et barn. Ikke still åpne spørsmål etc.
'''

from llm import Llm


# Eksempel 1: En stor prompt
def categorize(d: str) -> list:
    
    # Prompt der LLMen blir bedt om å dele inn i fire passende kategorier basert på artikkel-beskrivelse
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

response = Llm.llm.invoke(task).content
return response 


obj = categorize(d)