class SessionMemory:
    """Tracks conversation history."""

    def __init__(self):
        self.sessions = {"default": {"history": []}}

    def get(self, session_id="default"):
        return self.sessions[session_id]

    def add(self, role: str, text: str, session_id="default"):
        self.sessions[session_id]["history"].append({"role": role, "text": text})
