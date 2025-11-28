class Evaluator:
    """Ensures safety, clarity, and correctness."""

    def evaluate(self, candidate: dict):
        text = " ".join([str(v) for v in candidate.values()])

        flags = []
        if len(text) > 600:
            flags.append("too_long")

        emergency_words = ["suicide", "kill", "hurt", "911"]
        if any(w in text.lower() for w in emergency_words):
            flags.append("unsafe")

        approved = len(flags) == 0

        return {
            "approved": approved,
            "flags": flags,
            "candidate": candidate
        }
