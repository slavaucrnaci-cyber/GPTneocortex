class Memory:
    def __init__(self):
        self.traces = []

    def store_trace(self, trace):
        self.traces.append(trace)

    def get_traces(self):
        return self.traces

    def search(self, query):
        # 🔥 пока тупо возвращаем все
        # потом сделаем умный поиск (или mempalace)
        return self.traces