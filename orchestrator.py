from agents.persona import PersonaAgent
from agents.gap import GapAnalysisAgent
from agents.planner import PlannerAgent
from agents.learning import LearningAgent
from agents.project import ProjectAgent
from agents.application import ApplicationAgent
from agents.networking import NetworkingAgent
from agents.evaluator import EvaluatorAgent
from memory.store import MemoryStore

class Orchestrator:
    """
    The central brain of Shadow OS.
    Manages the lifecycle: Act -> Learn -> Adapt.
    """
    def __init__(self):
        self.memory = MemoryStore()
        
        # Initialize Agents
        self.persona_agent = PersonaAgent(self.memory)
        self.gap_agent = GapAnalysisAgent(self.memory)
        self.planner_agent = PlannerAgent(self.memory)
        
        # Execution Agents
        self.learning_agent = LearningAgent(self.memory)
        self.project_agent = ProjectAgent(self.memory)
        self.application_agent = ApplicationAgent(self.memory)
        self.networking_agent = NetworkingAgent(self.memory)
        
        self.evaluator_agent = EvaluatorAgent(self.memory)

    def run_initialization(self, current_data, shadow_data):
        """
        Phase 1: Initialization & Planning
        """
        print("\n--- [System Boot] Initializing Shadow OS ---")
        
        # 1. Persona Definition
        context = {"current_persona": current_data, "shadow_persona": shadow_data}
        self.persona_agent.process(context)
        
        # 2. Gap Analysis
        self.gap_agent.process()
        
        # 3. Planning
        plan_result = self.planner_agent.process()
        print("\n--- [Plan Generated] ---")
        return plan_result.get("roadmap", [])

    def run_execution_cycle(self):
        """
        Phase 2: Execution & Monitoring Loop
        """
        print("\n--- [Execution Cycle] Activating Agents ---")
        
        state = self.memory.get_state()
        roadmap = state.get("roadmap", [])
        
        if not roadmap:
            print("No roadmap found. Run initialization first.")
            return

        # Simple Demo Loop: Execute first 3 items
        for task in roadmap[:3]:
            print(f"\n>> Executing Task: {task['phase']} - {task['action']}")
            
            context = {"current_task": task}
            
            # Dispatch based on action type
            if task["action"] == "Learn":
                self.learning_agent.process(context)
            elif task["action"] == "Build":
                self.project_agent.process(context)
            elif task["action"] == "Role":
                self.application_agent.process(context)
            
            # Always run networking parallel
            self.networking_agent.process()
            
            # Evaluate after each step
            eval_result = self.evaluator_agent.process()
            print(f">> Evaluation: {eval_result['feedback']}")
            
        print("\n--- [Cycle Complete] Awaiting further instructions ---")
