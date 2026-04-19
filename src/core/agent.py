from src.core.orchestrator import Orchestrator
from src.core.evaluator import Evaluator

class Agent:

    def rewrite(self, text):
        clean = text.split("\n")[-1]
        return f"Resolve emotional tension:\n{clean}"

    def __init__(self, memory):
        self.memory = memory
        self.orchestrator = Orchestrator()
        self.evaluator = Evaluator()
        self.max_iters = 3

    def run(self, message, state):

        feedback = None
        best_score = 0
        best_message = message

        for i in range(self.max_iters):

            # 🔍 retrieval
            retrieved_memory = self.memory.search(message.text)

            # 🧠 planning
            plan = self.orchestrator.planner.plan(message, feedback, state)

            # ⚙️ execution
            message = self.orchestrator.run_with_plan(message, state, plan)

            if message is None:
                print("💥 Agent received None — stopping")
                return None

            # 📊 evaluation
            evaluation = self.evaluator.evaluate(message, state)
            score = evaluation.get("score", 0)

            # 🧬 trace (как dict, без усложнения)
            trace = {
                "input": message.text,
                "strategy": plan["plan"],
                "retrieved": retrieved_memory,
                "state": state.global_meta.copy(),
                "output": message.text,
                "score": score
            }

            # 💾 сохраняем только хорошие
            if score > 0.6:
                self.memory.store_trace(trace)

            # 🏆 лучший результат
            if score > best_score:
                best_score = score
                best_message = message
                state.global_meta["last_score"] = score

            print(f"\n[ITER {i}] PLAN:", plan)
            print(f"[ITER {i}] EVAL:", evaluation)

            # 🛑 stop condition
            if score > 0.75:
                break

            # 🔁 feedback loop
            feedback = evaluation
            message.text = self.rewrite(message.text)

        return best_message