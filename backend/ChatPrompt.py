from langchain_core.prompts import ChatPromptTemplate

def render_prompt(prompt: str):
    return  ChatPromptTemplate.from_template(prompt)