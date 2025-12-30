from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from core.orchestrator import CentralOrchestrator
import shutil
import os
import json

app = FastAPI()

# Allow CORS for local development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve UI files
app.mount("/ui", StaticFiles(directory="ui", html=True), name="ui")

@app.post("/upload_resume")
async def upload_resume(target_role: str = Form(...), file: UploadFile = File(...)):
    try:
        # Save file temporarily
        file_path = f"data/{file.filename}"
        os.makedirs("data", exist_ok=True)
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
            
        # Extract Text (Mocking for Demo using simple read or pypdf if available)
        text_content = ""
        if file.filename.endswith(".txt"):
             with open(file_path, "r", encoding="utf-8") as f:
                 text_content = f.read()
        else:
            # Fallback/Mock for PDF/Docx if libs missing in restricted env
            # In a real app we'd use pypdf
            try:
                from pypdf import PdfReader
                reader = PdfReader(file_path)
                for page in reader.pages:
                    text_content += page.extract_text() + "\n"
            except ImportError:
                print("pypdf not found, using mock content")
                text_content = "Mocked Resume Content: Skills: Python, Java. Experience: 2 Years."

        # Initialize OS
        orchestrator = CentralOrchestrator()
        
        # Prepare Input
        user_input = {
            "role": "Candidate", 
            "target_role": target_role,
            "resume_text": text_content,
            "skills": [] 
        }
        
        # Run Pipeline
        print("Running pipeline...")
        result = orchestrator.run_pipeline(user_input)
        
        # Construct Response
        response = {
            "status": "success",
            "profile": result["profile"],
            "roadmap": result["roadmap"],
            "convergence": result["convergence"],
            "logs": result["logs"],
            # Return specific data structures used by UI
            "verified_skills": orchestrator.state_manager.load_state().get("verified_skills", {}),
            "gaps": orchestrator.state_manager.load_state().get("gaps", []),
            "resources": orchestrator.state_manager.load_state().get("resources", [])
        }
        
        return response

    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
