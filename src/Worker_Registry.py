class WorkerRegistry:

    def __init__(self):
        self.workers = {}

    def register(self, worker):
        self.workers[worker.name] = worker

    def get(self, name):
        return self.workers.get(name)
    