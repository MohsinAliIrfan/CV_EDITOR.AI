from ChatPrompt import render_prompt
from .template import agent_prompt
from ai.main_Agent import MainAgent

class Extract_Keywords_Agent(MainAgent):
    
    def __init__(self, job_description: str):
        print("Extracting Keywords...")
        
        job_description = self.remove_curly_brackets(job_description)
        self.prompt = self.get_prompt(agent_prompt)
        
        input_dic = {
            'text' : job_description
        }
        
        super().__init__(self.prompt, input_dic)
            
        self.runAgent()
    
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