class Planner:
    """Interprets user input and produces a structured plan for the Worker."""

    def plan(self, user_input: str):
        text = user_input.lower()

        if "remind" in text or "reminder" in text or "alarm" in text:
            intent = "set_reminder"
            task = "generate_reminder"

        elif "how do i" in text or "how to" in text or "help" in text:
            intent = "tech_help"
            task = "generate_guide"

        elif "near" in text or "find" in text or "local" in text:
            intent = "resource_search"
            task = "search_resources"

        else:
            intent = "general"
            task = "respond_general"

        return {
            "intent": intent,
            "worker_task": task,
            "requires_tools": [],
            "user_input": user_input
        }
