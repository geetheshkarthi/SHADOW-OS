from .base import BaseAgent
from typing import Dict, Any, List

class ExecutionAgent(BaseAgent):
    def __init__(self):
        super().__init__("ExecutionAgent")

    def run(self, context: Dict[str, Any]) -> Dict[str, Any]:
        self.log("Finding resources for current milestones...")
        
        roadmap = context.get("roadmap", [])
        if not roadmap:
            return {"action_plan": []}
            
        current_phase = roadmap[0]
        milestones = current_phase.get("milestones", [])
        
        resources = []
        for m in milestones:
            # Mock resource finding
            resources.append({
                "milestone": m,
                "resources": [
                    {"type": "Course", "title": f"Advanced {m.split()[1]} Guide", "url": "http://mooc.com/course"},
                    {"type": "Project", "title": f"{m} Practice Repo", "url": "http://github.com/practice"}
                ]
            })
            
        self.log("Resources found.")
        return {"resources": resources}
