class SynthesisWorker:

    def __init__(self):
        self.name = "synthesis"

    def run(self, message, state):
        message.text = f"Final integrated response:\n{message.text}"

        message.trace.append({
            "step": "synthesis",
            "data": message.text
        })

        return message