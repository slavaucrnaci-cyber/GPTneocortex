class SensoryWorker:

    def __init__(self):
        self.name = "sensory" 
    

    def run(self, message, state):
        message.text = message.text.strip().lower()
        message.add_trace(self.name, message.text)
        return message
    
 # assert message is not None, "Worker broke message"