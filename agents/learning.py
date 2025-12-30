from .base import BaseAgent

class LearningAgent(BaseAgent):
    """
    Recommends specific learning resources (courses, papers, docs).
    """
    def __init__(self, memory):
        super().__init__("LearningAgent", memory)

    def process(self, context=None):
        task = context.get("current_task")
        if task and task["action"] == "Learn":
            topic = task["target"]
            self.log(f"Curating learning path for: {topic}")
            
            # Mock resource generation
            resources = [
                f"Course: Advanced {topic} on Coursera",
                f"Paper: Attention Is All You Need (foundational for {topic})",
                f"Docs: Hidiingface Transformers for {topic}"
            ]
            self.memory.log_outcome("Learning Recommendation", "Success", f"Recommended: {resources}")
            return {"status": "success", "resources": resources}
        
        return {"status": "skipped", "reason": "No active learning task"}
