from .base import BaseAgent
from typing import Dict, Any, List

class ResumeAgent(BaseAgent):
    def __init__(self):
        super().__init__("ResumeAgent")

    def run(self, context: Dict[str, Any]) -> Dict[str, Any]:
        self.log("Analyzing resume content...")
        
        resume_text = context.get("resume_text", "").lower()
        
        # Mock resume parsing logic
        # In a real scenario, this uses NER models
        known_skills = ["python", "java", "git", "sql", "tensorflow", "pytorch", "communication", "project management"]
        extracted = [skill for skill in known_skills if skill in resume_text]
        
        # Simple experience level heuristic
        experience_level = "Entry"
        if "senior" in resume_text or "lead" in resume_text:
            experience_level = "Senior"
        elif "years" in resume_text:
            # basic check
            experience_level = "Intermediate"

        self.log(f"Extracted Skills: {extracted}")
        return {
            "resume_skills": extracted,
            "experience_level": experience_level
        }
