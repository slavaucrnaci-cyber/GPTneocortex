class CognitiveWorker:

    def __init__(self):
        self.name = "cognitive"

    def run(self, message, state):
        message.text = (
            "Even though I feel fear and stuck, this is a temporary state. "
            "I can take a small action despite uncertainty."
        )

        message.trace.append({
            "step": "cognitive",
            "data": message.text
        })

        return message