from fastapi import FastAPI, File, UploadFile, Form, Request
from fastapi.responses import JSONResponse, FileResponse
from fastapi.middleware.cors import CORSMiddleware
import os
import sys

groq_api_key = os.getenv('GROQ_API_KEY')

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'backend')))
from main import Main

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = os.path.join(os.path.dirname(__file__), '..', 'backend', 'cvs_pdf_and_doc')
os.makedirs(UPLOAD_DIR, exist_ok=True)

final_result = ""  
main_object = Main()

@app.post("/process-cv/")
async def process_cv(url: str = Form(None), cv: UploadFile = File(None)): 
    global final_result
    
    if url and cv:
        file_path = os.path.join(UPLOAD_DIR, cv.filename)
        with open(file_path, "wb") as file:
            file.write(await cv.read()) 

        main_object.set_values(url, cv.filename)
        final_result = main_object.main()
        
        if final_result == "CV UPDATED SUCCESSFULLY":
            print("\n\nFINAL OUTPUT: ", final_result)
            return JSONResponse(content={"message": "CV UPDATED SUCCESSFULLY"}, status_code=200)

    return JSONResponse(content={"message": "UNABLE TO PROCESS"})

@app.get("/download-cv/")
async def download_cv(filename: str):
    file_path = os.path.join(UPLOAD_DIR, filename)

    if os.path.exists(file_path):
        return FileResponse(file_path, media_type="application/octet-stream", filename=filename)
    
    return JSONResponse(content={"message": "File not found"}, status_code=404)

@app.post("/chat_bot/")
async def chat_bot(request: Request):
    global final_result 
    
    body = await request.json() 
    user_query = body.get("user_query") 

    if not user_query:
        return JSONResponse(content={"message": "ENTER A QUERY."}, status_code=422)
    
    if final_result == "CV UPDATED SUCCESSFULLY":
        chat_response = main_object.chat_agent(user_query) 
        print("\nChat response: ", chat_response)
        return JSONResponse(content={"message": chat_response}, status_code=200)

    return JSONResponse(content={"message": "UNABLE TO PROCESS."}, status_code=200)
