from project.tools.tools import TimeParser, GuideGenerator, SearchTool

class Worker:
    """Executes tasks created by the Planner."""

    def __init__(self):
        self.time_parser = TimeParser()
        self.guide_gen = GuideGenerator()
        self.search_tool = SearchTool()

    def perform(self, plan: dict):
        task = plan["worker_task"]
        text = plan["user_input"]

        if task == "generate_reminder":
            parsed = self.time_parser.parse(text)
            if parsed:
                return {
                    "type": "reminder",
                    "message": f"I will remind you at {parsed}."
                }
            return {
                "type": "ask_time",
                "message": "What time would you like the reminder?"
            }

        elif task == "generate_guide":
            guide = self.guide_gen.create(text)
            return {
                "type": "guide",
                "title": guide["title"],
                "steps": guide["steps"],
                "message": guide["summary"]
            }

        elif task == "search_resources":
            results = self.search_tool.search(text)
            return {
                "type": "resources",
                "results": results,
                "message": f"I found {len(results)} helpful places."
            }

        return {
            "type": "general",
            "message": "I'm here to help! You can ask for reminders or simple tech instructions."
        }
