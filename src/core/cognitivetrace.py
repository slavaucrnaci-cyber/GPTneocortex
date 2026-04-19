class CognitiveTrace:
    def __init__(
        self,
        input_text,
        strategy,
        retrieved,
        state_snapshot,
        output,
        score
    ):
        self.input = input_text
        self.strategy = strategy
        self.retrieved = retrieved
        self.state = state_snapshot
        self.output = output
        self.score = score