class Message:
    def __init__(self, text: str):
        self.text = text
        self.meta = {}
        self.trace = []

    def add_trace(self, step, data):
        self.trace.append({
            "step": step,
            "data": data
        })