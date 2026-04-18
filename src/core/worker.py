class Worker:
    def __init__(self, name):
        self.name = name

    def run(self, message, state):
        message.text = "..."

        message.trace.append({
        "step": "shadow",
        "data": message.text
    })

        return message