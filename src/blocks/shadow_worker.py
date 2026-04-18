class ShadowWorker:

    def __init__(self):
        self.name = "shadow"

    def run(self, message, state):
        print("🔥 NEW SHADOW WORKING")

        text = message.text.lower()

        if "fear" in text:
            message.text = "I feel fear and uncertainty, and it's difficult to act."

        elif "uncertainty" in text:
            message.text = (
                "Uncertainty is present, but I can move forward step by step "
                "without needing full clarity."
            )

        message.trace.append({
            "step": "shadow",
            "data": message.text
        })

        return message