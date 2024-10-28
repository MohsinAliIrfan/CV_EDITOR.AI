from Project_manager.project_manager import ProjectManager
from dotenv import load_dotenv
import os
load_dotenv()

class Main(ProjectManager):
    
    def __init__(self):
        pass
        
    def set_values(self, url: str, cv_file_name: str):
        file_path = os.path.join(os.path.dirname(__file__), 'cvs_pdf_and_doc' , cv_file_name)
        print("URL IN MAIN", url, "  and file name: ", cv_file_name)
        super().__init__(url, file_path)
        
    
    def chat_agent(self, user_query: str):
        print("\n USER QUERY: ", user_query)
        return super().chat_with_ai_bot(user_query)
        
    def main(self):
       final_result = super().manage_project()
       print("\nfinal output:", final_result)
       
       return final_result

    