from core.orchestrator import CentralOrchestrator
import json

def main():
    print("Initializing Shadow OS (Extended)...")
    orchestrator = CentralOrchestrator()
    
    # Extended Demo Scenario
    resume_text = """
    John Doe
    Python Developer
    Experience: 2 years working with Python, Flask, and SQL.
    Projects: Built a chatbot using OpenAI API.
    Skills: Git, Python, Basic Java.
    """
    
    user_input = {
        "role": "Python Developer",
        "target_role": "AI Engineer",
        "resume_text": resume_text,
        "skills": [] # Will be populated from resume
    }
    
    print(f"User Input Resume Length: {len(resume_text)} chars")
    
    result = orchestrator.run_pipeline(user_input)
    
    # Output results for verification
    print("\n--- Final Output ---")
    print(f"Verified Skills: {result['profile']['skills']}")
    print(f"Convergence Score: {result['convergence'] * 100:.1f}%")
    print(f"Total Logs: {len(result['logs'])}")

if __name__ == "__main__":
    main()
