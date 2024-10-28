from ChatPrompt import render_prompt
from .template import agent_prompt
from ai.main_Agent import MainAgent

class ChatAgent(MainAgent):
    
    def __init__(self, 
                 user_query: str, 
                 cv_text: str,
                 job_description: str, 
                 extracted_keywords: str,
                 changed_cv_text: str):
        print("Chat Agent called...")
        
        user_query = self.remove_curly_brackets(user_query)
        cv_text = self.remove_curly_brackets(cv_text)
        job_description = self.remove_curly_brackets(job_description)
        changed_cv_text = self.remove_curly_brackets(changed_cv_text)
        
        self.prompt = self.get_prompt(agent_prompt)
        
        input_dict = {
            'user_query':user_query,
            'cv_text': 'Not provided',
            'job_description': 'Not provided',
            'extracted_keywords': extracted_keywords,
            'changed_cv_text': 'Not provided',
        }
        
        #The out for the LLM might surpass the limit if we provide everything in the input so having conditions we can always update the input_dict with the relevant input
        #in accordance to what the user has asked for
        if any(keyword in user_query.lower() for keyword in ('cv', 'resume', 'skills', 'skill')):
            input_dict['cv_text'] = cv_text
            
        if any(keyword in user_query.lower() for keyword in ('job description', 'job')):
            input_dict['job_description'] = job_description
        
        if any(keyword in user_query.lower() for keyword in ('changes', 'change', 'modified', 'modification')):
            input_dict['changed_cv_text'] = changed_cv_text
        
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