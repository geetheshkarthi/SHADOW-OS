from .base import BaseAgent
from core.roles import ROLES_DB
from typing import Dict, Any, List

class GapAnalysisAgent(BaseAgent):
    def __init__(self):
        super().__init__("GapAnalysisAgent")

    def run(self, context: Dict[str, Any]) -> Dict[str, Any]:
        self.log("Running Mathematical Gap Analysis...")
        
        profile = context.get("profile", {})
        verified_skills = context.get("verified_skills", {})
        resume_text = context.get("resume_text", "").lower()
        target_role = profile.get("target_role", "AI Engineer") 
        
        required = ROLES_DB.get(target_role, set())
        
        # 1. Define Base Strength (0.0 - 0.9)
        BASE_STRENGTH = {
            "None": 0.0, "Basic": 0.3, "Intermediate": 0.6, "Advanced": 0.9
        }
        
        # 2. Define Evidence Signals (Boosts)
        SIGNALS = {
            "transformer": ["deep learning", "nlp", "pytorch", "tensorflow"],
            "gan": ["deep learning", "pytorch", "tensorflow"],
            "bert": ["nlp", "transformers"],
            "gpt": ["nlp", "transformers", "llm"],
            "publication": ["research", "deep learning"],
            "deployed": ["mlops", "docker", "kubernetes"],
            "scale": ["system design", "distributed systems"],
            "optimization": ["system design", "algorithms"]
        }

        gaps = []
        
        for req in required:
            # A. Calculate Skill Strength
            level_str = "None"
            # Case-insensitive match from verified skills
            for v_skill, v_level in verified_skills.items():
                if v_skill.lower() == req.lower():
                    level_str = v_level
                    break
            
            base = BASE_STRENGTH.get(level_str, 0.0)
            
            # Evidence Boost
            boost = 0.0
            found_signals = []
            for signal, linked_skills in SIGNALS.items():
                if signal in resume_text:
                    for linked in linked_skills:
                        if linked in req.lower() or req.lower() in linked:
                            # Found a relevant signal
                            boost = 0.2 # Standard boost per signal type
                            if signal not in found_signals: found_signals.append(signal)

            skill_strength = min(1.0, base + boost)
            
            # B. Calculate Gap Value
            required_level = 1.0 # We assume target is Mastery
            gap_value = required_level - skill_strength
            
            # C. Determine Gap Type
            # Strict Thresholds
            if gap_value >= 0.6:
                gap_type = "Critical Deficit"
                severity = "High"
            elif gap_value >= 0.3:
                gap_type = "Weak Foundation"
                severity = "Medium"
            elif gap_value > 0.0:
                gap_type = "Refinement Needed"
                severity = "Low"
            else:
                gap_type = "Scaling Opportunity"
                severity = "None" # Skill is met/exceeded
            
            if gap_type != "Scaling Opportunity":
                 gaps.append({
                     "skill": req,
                     "skill_strength": round(skill_strength, 2),
                     "required_level": required_level,
                     "gap_value": round(gap_value, 2),
                     "gap_type": gap_type,
                     "severity": severity,
                     "signals": found_signals
                 })

        # 3. Sort by Gap Value Descending (Most critical first)
        gaps.sort(key=lambda x: x["gap_value"], reverse=True)
        
        self.log(f"Math Analysis Complete. Top Gap: {gaps[0]['skill'] if gaps else 'None'} ({gaps[0]['gap_value'] if gaps else 0.0})")
        return {"gaps": gaps}
