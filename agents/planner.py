from .base import BaseAgent
from typing import Dict, Any, List

class PlannerAgent(BaseAgent):
    def __init__(self):
        super().__init__("PlannerAgent")

    def run(self, context: Dict[str, Any]) -> Dict[str, Any]:
        self.log("Constructing Dynamic Roadmap from Gap Ranking...")
        
        # 1. Ingest Ranked Gaps (Source of Truth)
        # We DO NOT look at "Target Role". We only look at "What is missing".
        gaps = context.get("gaps", [])
        
        if not gaps:
            self.log("No gaps. Providing Mastery Maintenance Plan.")
            return {"roadmap": [{
                "phase": 1, "goal": "System Mastery & Leadership", "duration_months": 3,
                "milestones": ["Lead architecture methodology", "Publish research", "Mentor seniors"]
            }]}

        roadmap = []
        phase_counter = 1
        
        # 2. Dynamic Chunking based on Gap Type
        # We iterate through the specific gaps found for THIS user.
        
        # Priority 1: Critical Deficits (Must fix first)
        critical_gaps = [g for g in gaps if g['gap_type'] == "Critical Deficit"]
        if critical_gaps:
             skills = [g['skill'] for g in critical_gaps]
             roadmap.append({
                 "phase": phase_counter,
                 "goal": "Urgent Foundational Reconstruction",
                 "duration_months": max(3, len(skills) * 1.5),
                 "milestones": [
                     f"Intensive 0-to-1 Bootcamp: {', '.join(skills[:3])}",
                     "Pass fundamental assessments",
                     "Build 'Hello World' equivalent for each stack"
                 ]
             })
             phase_counter += 1
             
        # Priority 2: Weak Foundations (Build competence)
        weak_gaps = [g for g in gaps if g['gap_type'] == "Weak Foundation"]
        if weak_gaps:
             skills = [g['skill'] for g in weak_gaps]
             roadmap.append({
                 "phase": phase_counter,
                 "goal": "Competency & Application",
                 "duration_months": len(skills) * 1,
                 "milestones": [
                     f"Building Mini-Projects for: {', '.join(skills[:3])}",
                     "Refactoring existing codebases",
                     "Contributing to relevant documentation"
                 ]
             })
             phase_counter += 1
             
        # Priority 3: Refinement (Polish)
        refine_gaps = [g for g in gaps if g['gap_type'] == "Refinement Needed"]
        if refine_gaps or (not critical_gaps and not weak_gaps):
             # If we are here, user is decent.
             skills = [g['skill'] for g in refine_gaps] if refine_gaps else [g['skill'] for g in gaps[:3]]
             roadmap.append({
                 "phase": phase_counter,
                 "goal": "System Optimization & Scaling",
                 "duration_months": 3,
                 "milestones": [
                     f"Production-grade deployment of: {', '.join(skills[:3])}",
                     "Performance auditing and latency optimization",
                     "Implementing CI/CD pipelines"
                 ]
             })
             phase_counter += 1

        # Final Capstone (Always present, content depends on user's STRONGEST skills)
        roadmap.append({
            "phase": phase_counter,
            "goal": "Capstone: Market Readiness",
            "duration_months": 2,
            "milestones": [
                "Deploy full-stack portfolio project",
                "Technical Interview Prep (System Design)",
                "Outreach and networking"
            ]
        })
        
        self.log(f"Roadmap Constructed: {len(roadmap)} Phases.")
        return {"roadmap": roadmap}
