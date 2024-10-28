from ChatPrompt import render_prompt
from .template import agent_prompt
from ai.main_Agent import MainAgent

class Extract_Job_Description(MainAgent):
    
    def __init__(self, web_page: str):
        print("Extract_Job_Description...")
        
        web_page = self.remove_curly_brackets(web_page)
        self.prompt = self.get_prompt(agent_prompt)
        
        input_dict = {
            'web_page':web_page
        }
        
        super().__init__(self.prompt, input_dict)
    
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