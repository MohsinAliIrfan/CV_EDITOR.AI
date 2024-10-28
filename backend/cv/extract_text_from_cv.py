from docx import Document
import docx
import os


class ExtractTextFromCV():
    def __init__(self) -> None:
        file_path = os.path.join(os.path.dirname(__file__), '..', 'cvs_pdf_and_doc', 'Output.docx')
        if not os.path.exists(file_path):
            raise ValueError("Please provide a valid file path.")
        
        else:
            self.file_path = file_path

    def extract_text(self) -> str:
        
        if os.path.exists(self.file_path):
            
            doc = docx.Document(self.file_path)
            fullText = []
            
            for para in doc.paragraphs:
                fullText.append(para.text)
            
            return '\n'.join(fullText)
        
        else:
            return 'NO PATH FOUND'
        