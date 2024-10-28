from pdf2docx import Converter
from docx import Document
import os
 
class CVCconverter():
    
    def __init__(self, file_path: str) -> None:
        self.cv_file = file_path
        self.output_file = os.path.join(os.path.dirname(__file__), 'Output.docx')
    
    def pdf_to_docx(self) -> bool:
        try:
            cv = Converter(self.cv_file)
            cv.convert(self.output_file, start=0, end=None) 
            cv.close()
            return True
        except Exception as e:
            print("\nWhile converting the file, the following error occured: ", e)
            return False

    def replace_text_keep_format(self, replace_dict: dict) -> bool:
        
        try:
            doc = Document(self.output_file)
        
            for p in doc.paragraphs:
                for run in p.runs: 
                    for word in replace_dict:
                        if word in run.text:
                            run.text = run.text.replace(word, replace_dict[word])
                            
            doc.save(os.path.join(os.path.dirname(__file__), 'final_output.docx'))
            return True        
        except Exception as e:
            print("\nWhile replacing the text, the following error occured: ", e)
            return False
                        



