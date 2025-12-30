from .base import BaseAgent

class ApplicationAgent(BaseAgent):
    """
    Optimizes resume and application strategy.
    Does NOT auto-apply.
    """
    def __init__(self, memory):
        super().__init__("ApplicationAgent", memory)

    def process(self, context=None):
        task = context.get("current_task")
        if task and task["action"] == "Role":
            role = task["target"]
            self.log(f"Formulating application strategy for: {role}")
            
            # Retrieve winning strategies from memory
            strategies = self.memory.get_state().get("strategy_rules", ["Default: Tailor Resume"])
            
            advice = [
                f"Optimize LinkedIn Headline for {role}",
                "Reach out to 2 recruiters/week",
                f"Apply Strategy: {strategies[-1]}"
            ]
            
            self.memory.log_outcome("Application Strategy", "Ready", f"Advice generated for {role}")
            return {"status": "success", "advice": advice}
            
        return {"status": "skipped", "reason": "Not in application phase"}
