from .base import BaseAgent

class ProjectAgent(BaseAgent):
    """
    Suggests high-impact projects that demonstrate required skills.
    """
    def __init__(self, memory):
        super().__init__("ProjectAgent", memory)

    def process(self, context=None):
        task = context.get("current_task")
        if task and task["action"] == "Build":
            topic = task["target"]
            self.log(f"Designing project scope for: {topic}")
            
            project_idea = {
                "title": f"{topic} - RAG Pipeline",
                "tech_stack": ["LangChain", "Pinecone", "OpenAI API"],
                "deliverable": "GitHub Repo + Live Streamlit Demo"
            }
            
            self.memory.log_outcome("Project Definition", "Success", f"Defined: {project_idea['title']}")
            return {"status": "success", "project": project_idea}
            
        return {"status": "skipped", "reason": "No active build task"}
