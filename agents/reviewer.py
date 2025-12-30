from .base import BaseAgent
from core.roles import ROLES_DB
from typing import Dict, Any, List

class ReviewAgent(BaseAgent):
    def __init__(self):
        super().__init__("ReviewAgent")

    def run(self, context: Dict[str, Any]) -> Dict[str, Any]:
        self.log("Calculating Convergence Score & Reviewing Progress...")
        
        profile = context.get("profile", {})
        verified_skills = context.get("verified_skills", {})
        target_role = profile.get("target_role", "AI Engineer")
        
        # Convergence Score Calculation
        # Dynamic: (Sum of All Verified Skill Scores) / (Total Required Skills * Max Score)
        
        required_skills = ROLES_DB.get(target_role, set())
        total_possible_score = len(required_skills) * 1.0 # 1.0 is max per skill
        
        current_total_score = 0.0
        prof_map = {"None": 0.0, "Basic": 0.3, "Intermediate": 0.7, "Advanced": 1.0}
        
        for req in required_skills:
            # Find level
            level = "None"
            for v_skill, v_level in verified_skills.items():
                 if v_skill.lower() == req.lower():
                     level = v_level
                     break
            current_total_score += prof_map.get(level, 0.0)
            
        if total_possible_score <= 0:
            convergence_score = 0.0
        else:
            convergence_score = current_total_score / total_possible_score
            
        convergence_score = min(max(convergence_score, 0.0), 1.0) # Clamp
        
        self.log(f"Dynamic Convergence Score: {convergence_score*100:.1f}% ({current_total_score:.1f}/{total_possible_score})")
        
        # Failure/Success Logic
        status = "GREEN"
        if convergence_score < 0.3: # Slightly higher threshold for "Red"
            status = "RED"
            self.log("Critical Alert: Signal is low. Strategy shift required.")
            
        return {
            "status": status,
            "convergence_score": convergence_score,
            "adjustment_needed": status == "RED"
        }
