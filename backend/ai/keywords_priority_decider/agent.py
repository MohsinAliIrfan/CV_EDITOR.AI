from ChatPrompt import render_prompt
from .template import agent_prompt
from ai.main_Agent import MainAgent

class DecidePriorityKeywords(MainAgent):
    
    def __init__(self, job_description: str, keywords: list):
        print("\n\n\n Getting Priority Keywrods")
        
        job_description = str(job_description)
        keywords = str(keywords)
        job_description = self.remove_curly_brackets(job_description)
        keywords = self.remove_curly_brackets(keywords)
        
        self.prompt = self.get_prompt(agent_prompt)
        
        self.input_dic = {
            'extracted_keywords': keywords,
            'job_description': job_description
        }
        
        super().__init__(self.prompt, self.input_dic)
    
    
    def remove_curly_brackets(self, input_val: str) -> str:
        result = [] 

        for char in input_val:
            if char == '{':
                result.append('{{') 
            elif char == '}':
                result.append('}}') 
            else:
                result.append(char)  

        return ''.join(result)
    
    def get_prompt(self, agent_prompt: str):
        return render_prompt(agent_prompt)
        
    def runAgent(self):
        return super().runAgent()