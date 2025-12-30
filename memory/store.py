import json
import os
from datetime import datetime

class MemoryStore:
    """
    A simple, explainable persistent memory store using JSON.
    It holds the state of the Persona, Plan, Outcomes, and Strategy.
    """
    def __init__(self, filepath="memory.json"):
        self.filepath = filepath
        self.data = {
            "current_persona": {},
            "shadow_persona": {},
            "gaps": [],
            "roadmap": [],
            "outcome_history": [],
            "strategy_rules": []
        }
        self.load()

    def load(self):
        if os.path.exists(self.filepath):
            with open(self.filepath, 'r') as f:
                self.data = json.load(f)

    def save(self):
        with open(self.filepath, 'w') as f:
            json.dump(self.data, f, indent=4)

    def update_persona(self, current, shadow):
        self.data["current_persona"] = current
        self.data["shadow_persona"] = shadow
        self.save()

    def update_gaps(self, gaps):
        self.data["gaps"] = gaps
        self.save()

    def update_roadmap(self, roadmap):
        self.data["roadmap"] = roadmap
        self.save()

    def log_outcome(self, action, result, notes=""):
        entry = {
            "timestamp": datetime.now().isoformat(),
            "action": action,
            "result": result, # e.g., "Success", "Failure", "Pending"
            "notes": notes
        }
        self.data["outcome_history"].append(entry)
        self.save()

    def add_strategy_rule(self, rule):
        """
        Example rule: "If cold_email fails > 3 times, switch to content_marketing"
        """
        if rule not in self.data["strategy_rules"]:
            self.data["strategy_rules"].append(rule)
            self.save()

    def get_state(self):
        return self.data
