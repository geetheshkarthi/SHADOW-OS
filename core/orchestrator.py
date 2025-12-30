from agents.persona import PersonaAgent
from agents.resume import ResumeAgent
from agents.assessment import AssessmentAgent
from agents.gap import GapAnalysisAgent
from agents.planner import PlannerAgent
from agents.executor import ExecutionAgent
from agents.reviewer import ReviewAgent
from core.bus import EventBus
from memory.state import StateManager
from typing import Dict, Any, List
import datetime
import json

class CentralOrchestrator:
    def __init__(self):
        self.bus = EventBus()
        self.state_manager = StateManager()
        self.activity_log = []
        
        # Initialize Agents
        self.agents = {
            "resume": ResumeAgent(),
            "persona": PersonaAgent(),
            "assessment": AssessmentAgent(),
            "gap": GapAnalysisAgent(),
            "planner": PlannerAgent(),
            "executor": ExecutionAgent(),
            "reviewer": ReviewAgent()
        }

    def _log_activity(self, agent: str, action: str, details: str):
        entry = {
            "timestamp": datetime.datetime.now().isoformat(),
            "agent": agent,
            "action": action,
            "details": details
        }
        self.activity_log.append(entry)
        # Also persist log to file if needed, but in-memory is fine for this demo

    def run_pipeline(self, user_input: Dict[str, Any]):
        print("\n--- Starting Shadow OS Orchestration (Extended) ---")
        
        context = {"user_input": user_input, "profile": self.state_manager.load_state()}
        
        # 0. Resume Parsing (Optional but recommended)
        if "resume_text" in user_input:
            context["resume_text"] = user_input["resume_text"]
            resume_result = self.agents["resume"].run(context)
            # Merge extracted skills into input for Persona
            user_input["skills"] = list(set(user_input.get("skills", []) + resume_result["resume_skills"]))
            self._log_activity("ResumeAgent", "Parse", f"Extracted {len(resume_result['resume_skills'])} skills")

        # 1. Persona Profiling
        context["user_input"] = user_input # Updated with resume skills
        
        # CRITICAL: Force target_role from input to override any stale state
        if "target_role" in user_input:
             current_state = self.state_manager.load_state()
             current_state["target_role"] = user_input["target_role"]
             self.state_manager.save_state(current_state)
             
        profile_result = self.agents["persona"].run(context)
        self.state_manager.save_state(profile_result["profile"])
        context["profile"] = profile_result["profile"]
        self._log_activity("PersonaAgent", "Update", f"Target set to: {context['profile'].get('target_role')}")
        
        # 2. Skill Verification
        assess_result = self.agents["assessment"].run(context)
        context["verified_skills"] = assess_result["verified_skills"]
        self._log_activity("AssessmentAgent", "Verify", f"Verified {len(assess_result['verified_skills'])} skills")

        # 3. Gap Analysis
        gap_result = self.agents["gap"].run(context)
        context["gaps"] = gap_result["gaps"]
        self._log_activity("GapAnalysisAgent", "Analyze", f"Found {len(gap_result['gaps'])} gaps")
        
        # 4. Planning
        plan_result = self.agents["planner"].run(context)
        self.state_manager.update_key("roadmap", plan_result["roadmap"])
        context["roadmap"] = plan_result["roadmap"]
        self._log_activity("PlannerAgent", "Plan", f"Generated {len(plan_result['roadmap'])} phases")
        
        # 5. Execution (Resource Finder)
        exec_result = self.agents["executor"].run(context)
        self._log_activity("ExecutionAgent", "Search", f"Found resources for Phase 1")
        
        # 6. Review & Convergence
        review_result = self.agents["reviewer"].run(context)
        self._log_activity("ReviewAgent", "Evaluate", f"Convergence Score: {review_result['convergence_score']:.2f}")
        
        print("--- Orchestration Complete ---\n")
        
        # Save Activity Log for UI
        self.state_manager.update_key("activity_log", self.activity_log)
        self.state_manager.update_key("convergence_score", review_result["convergence_score"])
        self.state_manager.update_key("verified_skills", assess_result["verified_skills"])
        self.state_manager.update_key("gaps", gap_result["gaps"])
        self.state_manager.update_key("resources", exec_result["resources"])
        
        # EXPORT FOR UI (Bypassing CORS for local demo)
        full_state = {
            "profile": context["profile"],
            "roadmap": plan_result["roadmap"],
            "convergence": review_result["convergence_score"],
            "verified_skills": assess_result["verified_skills"],
            "gaps": gap_result["gaps"],
            "activity_log": self.activity_log,
            "resources": exec_result["resources"]
        }
        with open("ui/data.js", "w") as f:
            f.write(f"const SYSTEM_DATA = {json.dumps(full_state, indent=4)};")
        
        return {
            "profile": context["profile"],
            "roadmap": plan_result["roadmap"],
            "convergence": review_result["convergence_score"],
            "logs": self.activity_log
        }
