from ChatPrompt import render_prompt
from .template import agent_prompt
from ai.main_Agent import MainAgent

class OptimizeOutputAgent(MainAgent):
    
    def __init__(self, cv_text: str, priority_keywords: str, output_dict: str):
        print("\n\n OptimizeOutputAgent  called...")
        
        priority_keywords = str(priority_keywords)
        
        output_dict = str(output_dict)
        priority_keywords = str(priority_keywords)
        
        output_dict = self.remove_curly_brackets(output_dict)
        priority_keywords = self.remove_curly_brackets(priority_keywords)
        cv_text = self.remove_curly_brackets(cv_text)
        
        self.prompt = self.get_prompt(agent_prompt)
        
        self.input_dict = {
            'output_dict': output_dict,
            'extracted_keywords': priority_keywords,
            'cv_text': cv_text
        }
        
        super().__init__(self.prompt, self.input_dict)
    
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
        print("\n\n OptimizeOutputAgent RUN AGENT CALLED...")
        return super().runAgent()