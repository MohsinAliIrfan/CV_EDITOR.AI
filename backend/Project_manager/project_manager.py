import requests
import ast
import os
from bs4 import BeautifulSoup
from ai.extract_job_description.agent import Extract_Job_Description
from ai.extract_keywords_from_description.agent import Extract_Keywords_Agent
from cv.extract_text_from_cv import ExtractTextFromCV
from ai.words_to_be_replaced_with_keywords_decider.agent import ReplcaeWordswithKeyWordsDecider
from ai.keywords_priority_decider.agent import DecidePriorityKeywords
from ai.optimize_keywords.agent import OptimizeOutputAgent
from ai.chat_agent.agent import ChatAgent
from cvs_pdf_and_doc.pdftodocs import CVCconverter

class ProjectManager(CVCconverter):
    def __init__(self, url: str, file_path):
        self.url = url
        self.uploaded_cv = file_path
        super().__init__(file_path)
        
        
    def extract_web_page(self):
        counter = 0
        while counter < 5:
            print("\nExtracting all text from the website...\n")
            response = requests.get(self.url)
            if response.status_code != 200:
                counter += 1
                print(f"Failed to retrieve the page. Status code: {response.status_code}")
            else:
                soup = BeautifulSoup(response.content, 'html.parser')
                all_text = soup.get_text(separator='\n', strip=True)
                if all_text:
                    return all_text
                else:
                    return None

    def remove_similar_keywords(self, cv_text: str, keywords: list) -> list:
        print("\n\nREMOVING SIMILAR WORDS: ")
        for keyword in keywords:
            if keyword.lower() in cv_text.lower():
                print("\n\n Similar word: ", keyword)
                keywords.remove(keyword)
        return keywords


    def extract_job_description(self, extracted_text: str):
        counter = 0
        while counter < 5:
            job_description = Extract_Job_Description(extracted_text).runAgent()
            if job_description != 'NO JOB DESCRIPTION':
                self.job_description = job_description
                return job_description
            counter += 1
        return None

    def extract_keywords(self, job_description: str):
        counter = 0
        while counter < 5:
            keywords = Extract_Keywords_Agent(job_description).runAgent().split(',')
            print("\n Length of keywords: ", len(keywords))
            if len(keywords) <= 45:
                self.extracted_keywords = keywords
                return keywords
            counter += 1
            print("\n Number of keywords exceeds the limit, Trying again...")
        return []

    def decide_priority_keywords(self, job_description: str, updated_keywords: list):
        counter = 0
        while counter < 5:
            priority_keywords = DecidePriorityKeywords(job_description, updated_keywords).runAgent()
            dict_priority_keywords = ast.literal_eval(priority_keywords)#converting the output into a dict
            if isinstance(dict_priority_keywords['high_priority'], list) and dict_priority_keywords['high_priority']:
                return dict_priority_keywords
            counter += 1
        return {}

    def replace_words_with_keywords(self, cv_text: str, priority_keywords: dict):
        counter = 0
        while counter < 5:
            words_to_be_replaced = ReplcaeWordswithKeyWordsDecider(cv_text, priority_keywords).runAgent()
            print("\n\n Replcae words with keywords: ", words_to_be_replaced)
            try:
                words_to_be_replaced = ast.literal_eval(words_to_be_replaced)
                return words_to_be_replaced
            except Exception as e:
                counter += 1
                print("\n\n THE FOLLOWING ERROR OCCURED,", e)
        return {}

    def optimize_output(self, cv_text: str, priority_keywords: dict, words_to_be_replaced: dict):
        counter = 0
        while counter < 5:
            final_output = OptimizeOutputAgent(cv_text, priority_keywords, words_to_be_replaced).runAgent()
            print("\n\n\n Final OUTPUT: ", final_output)
            try:
                final_output_dict = ast.literal_eval(final_output)
                self.words_changed = final_output
                return final_output_dict
            except Exception as e:
                counter += 1
                print("\n\n THE FOLLOWING ERROR OCCURED,", e)
        
        return {}
    
    
    def chat_with_ai_bot(self, user_query: str) -> str:
        counter = 0
        while counter < 5:
            try:
                chat_bot_response = ChatAgent(user_query, self.cv_text, self.job_description,
                                              self.extracted_keywords, self.words_changed).runAgent()
                return chat_bot_response
            except Exception as e:
                counter +=1
                print("Unable to Chat with the agent...")
        
        return "CHAT BOT DID NOT RESPONSE..."        
            
        
    def manage_project(self, user_query: str = ''):
        print("Project Manager...")

        # Convert CV to DOCX
        super().__init__(self.uploaded_cv)
        convert_cv = super().pdf_to_docx()
        if not convert_cv:
            print("\n Failed to convert CV to DOCX")
            return "UNABLE TO CONVERT THE PDF TO A DOCX FILE"

        # Extract text from CV
        cv_text = ExtractTextFromCV().extract_text()
        if cv_text == "NO PATH FOUND":
            return "NO PATH FOUND"
        else:
            self.cv_text = cv_text
            print("\n\n THIS IS THE CV TEXT: ", cv_text)

        # Extract text from the webpage
        extracted_text = self.extract_web_page()
        if not extracted_text:
            return "UNABLE TO EXTRACT WEB PAGE"

        # Extract job description
        job_description = self.extract_job_description(extracted_text)
        if not job_description:
            return 'NO JOB DESCRIPTION'

        # Extract keywords
        keywords = self.extract_keywords(job_description)
        if not keywords:
            return "UNABLE TO EXTRACT KEYWORDS"

        # Remove similar keywords
        updated_keywords = self.remove_similar_keywords(cv_text, keywords)
        print("\n\n\n Updated Keywords: ", updated_keywords)

        # Decide priority keywords
        priority_keywords = self.decide_priority_keywords(job_description, updated_keywords)
        if not priority_keywords:
            return "UNABLE TO DECIDE PRIORITY KEYWORDS"

        # Replace words with keywords
        words_to_be_replaced = self.replace_words_with_keywords(cv_text, priority_keywords)
        if not words_to_be_replaced:
            return "UNABLE TO REPLACE WORDS WITH KEYWORDS"

        # Optimize output
        final_output = self.optimize_output(cv_text, priority_keywords, words_to_be_replaced)
        if final_output:
            success = super().replace_text_keep_format(final_output)
            if success:
                print("\n\nFinal output: ", final_output)
                return "CV UPDATED SUCCESSFULLY"
        

        return "UNABLE TO MODIFY THE CV, PLEASE TRY AGAIN"
