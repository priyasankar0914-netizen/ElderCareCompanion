class TimeParser:
    """Simple keyword-based time parser."""

    def parse(self, text: str):
        t = text.lower()
        if "morning" in t:
            return "8:00 AM"
        if "evening" in t:
            return "6:00 PM"
        if "afternoon" in t:
            return "3:00 PM"
        return None


class GuideGenerator:
    """Creates simple phone help instructions."""

    def create(self, text: str):
        t = text.lower()
        if "whatsapp" in t and "call" in t:
            return {
                "title": "How to start a WhatsApp video call",
                "steps": [
                    "Open WhatsApp.",
                    "Tap the person you want to call.",
                    "Tap the video icon at the top."
                ],
                "summary": "Open WhatsApp → Choose contact → Tap video icon."
            }
        return {
            "title": "Try this",
            "steps": ["Restart your device.", "Ensure your app is updated."],
            "summary": "Restart device and update app."
        }


class SearchTool:
    """Returns mock helpful community resources."""

    def search(self, text: str):
        return [
            {"name": "Community Senior Center", "phone": "123-456"},
            {"name": "Local Tech Help Volunteers", "phone": "555-888"}
        ]
