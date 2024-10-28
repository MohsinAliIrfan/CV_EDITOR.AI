# Welcome to CV_EDITOR.AI!

CV_EDITOR.AI is an innovative AI-based solution designed to enhance your CV according to job descriptions. The tool ensures your CV contains all the essential keywords to pass Applicant Tracking Systems (ATS) and increase your chances of landing that dream job

## Key Features

- **AI-Powered Modifications**: Leverages the powerful **LLaMA 3 (70B)** model via **Groq**.
- **LangChain Integration**: Utilizes LangChain for optimal performance.
- **Custom AI Agents**: Developed AI agents that utilize advanced prompt engineering and few-shot learning techniques to deliver the most relevant output.
- **User-Friendly Interface**: Runs smoothly on your localhost.

## How It Works

Simply provide your CV and the link to the webpage containing the job description. Our application will extract the job description using web scraping techniques, and AI agents will intelligently modify your CV accordingly.

Additionally, you can interact with the application through a chatbot feature, allowing for a more engaging user experienc

## Getting Started

1. **Obtain a GROQ_API_KEY**: Sign up at [Groq Console](https://console.groq.com/keys).
2. **Clone the Repository**: Pull the entire application.
3. **Configure Environment Variables**:
        a. Open the .env file located in the frontend directory.
        b. Paste your GROQ_API_KEY into this file.
   
5. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt

6. **Navigate to the Frontend:**
   ```bash
   cd frontend

7. **Run the Application:**
   ```bash
   uvicorn fastapp:app --reload --port 8001

8. **Access the Application**: Open interface.html in your web browser on localhost.
9. Enjoy the Experience!
![image](https://github.com/user-attachments/assets/e91dd16a-ad98-4e48-8e81-929f6b5181bb)
![image](https://github.com/user-attachments/assets/150b6a33-4d1a-4586-add9-26c486a5a389)

## **Need Help?**
If you encounter any errors, missing dependencies, or have questions related to the project, please feel free to contact me at mohsinaliirfan70@gmail.com.


   
