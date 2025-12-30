import json
import os
from typing import Dict, Any

class StateManager:
    def __init__(self, file_path: str = "data/user_profile.json"):
        self.file_path = file_path
        self._ensure_dir()

    def _ensure_dir(self):
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)

    def save_state(self, state: Dict[str, Any]):
        with open(self.file_path, "w") as f:
            json.dump(state, f, indent=4)

    def load_state(self) -> Dict[str, Any]:
        if not os.path.exists(self.file_path):
            return {}
        with open(self.file_path, "r") as f:
            return json.load(f)

    def update_key(self, key: str, value: Any):
        state = self.load_state()
        state[key] = value
        self.save_state(state)
