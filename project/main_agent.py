from project.agents.planner import Planner
from project.agents.worker import Worker
from project.agents.evaluator import Evaluator
from project.memory.session_memory import SessionMemory
from project.core.context_engineering import build_context
from project.core.observability import log

class MainAgent:
    def __init__(self):
        self.planner = Planner()
        self.worker = Worker()
        self.evaluator = Evaluator()
        self.memory = SessionMemory()

    def handle_message(self, user_input: str, session_id="default"):
        session = self.memory.get(session_id)

        plan = self.planner.plan(user_input)
        candidate = self.worker.perform(plan)
        evaluation = self.evaluator.evaluate(candidate)

        self.memory.add("user", user_input)
        self.memory.add("assistant", candidate.get("message", ""))

        log("plan", plan)
        log("candidate", candidate)
        log("evaluation", evaluation)

        if evaluation["approved"]:
            reply = candidate.get("message", "Okay.")
        else:
            reply = "I'm sorry, I can't answer that safely."

        return {"response": reply}

def run_agent(user_input: str):
    agent = MainAgent()
    result = agent.handle_message(user_input)
    return result["response"]
