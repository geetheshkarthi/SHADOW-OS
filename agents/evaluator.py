from .base import BaseAgent

class EvaluatorAgent(BaseAgent):
    """
    The Critic. Reviews outcomes, updates strategies, and closes the loop.
    """
    def __init__(self, memory):
        super().__init__("EvaluatorAgent", memory)

    def process(self, context=None):
        self.log("Evaluating recent cycle outcomes...")
        
        history = self.memory.get_state().get("outcome_history", [])
        if not history:
            return {"status": "neutral", "message": "No history to evaluate"}
        
        last_outcome = history[-1]
        self.log(f"Reviewing last action: {last_outcome['action']} -> {last_outcome['result']}")
        
        feedback = "Proceed"
        if last_outcome['result'] == "Failure":
            feedback = "Adapt Strategy"
            self.memory.add_strategy_rule(f"Avoid repeating {last_outcome['action']} without changes")
        
        return {"status": "success", "feedback": feedback}
