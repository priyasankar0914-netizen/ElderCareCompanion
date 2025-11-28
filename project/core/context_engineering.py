def build_context(user_input: str, session: dict):
    return {
        "user_input": user_input,
        "recent_messages": session["history"][-5:],
        "system_behavior": "Speak gently and offer simple steps."
    }
