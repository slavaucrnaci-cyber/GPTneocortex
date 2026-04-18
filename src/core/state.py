class AgentState:

    def __init__(self):
        self.messages = []
        self.history = []
        self.global_meta = {}

    def add_message(self, message):
        self.messages.append(message)

    def add_history(self, text, iteration):
        self.history.append({
            "input": text,
            "iteration": iteration
        })