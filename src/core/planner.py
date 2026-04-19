class LLMPlanner:

    def __init__(self, memory):
        self.memory = memory

    def plan(self, message, feedback=None, state=None, retrieved=None):

        # 1. используем уже переданный retrieval
        if retrieved:
            best = max(retrieved, key=lambda t: t["score"])
            return {"plan": best["strategy"]}

        # 2. fallback retrieval внутри
        similar = self.memory.search(message.text)

        if similar:
            best = max(similar, key=lambda t: t["score"])
            return {"plan": best["strategy"]}

        # 3. дефолт
        return {"plan": ["sensory", "synthesis"]}