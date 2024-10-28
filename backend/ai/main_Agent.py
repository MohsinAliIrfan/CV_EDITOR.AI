import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv

class MainAgent():
    
    def __init__(self, prompt: str, user_query: str, grok: str = "hello"):
        self.GROQ_API_KEY = os.getenv('GROQ_API_KEY')
        self.agents_prompt = prompt
        self.input_dict = user_query
        self.model = ChatGroq(model="llama3-70b-8192", temperature=0.0,  max_retries=1)
        
    
    def runAgent(self):
        chain = self.agents_prompt | self.model
        print("\nGetting response...")
        
        counter = 0
        while counter < 5:
            try:
                respone = chain.invoke(self.input_dict)
                return respone.content
            except Exception as e:
                counter+=1
                print(f"\n The following error: ' {e} '  while processing your request.")


    