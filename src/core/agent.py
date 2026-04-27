from src.core.orchestrator import Orchestrator
from src.core.evaluator import Evaluator

class Agent:

    def rewrite(self, text):
        clean = text.split("\n")[-1]
        return f"Resolve emotional tension:\n{clean}"

    def __init__(self, memory):
        self.memory = memory
        self.orchestrator = Orchestrator(self.memory)
        self.evaluator = Evaluator()
        self.max_iters = 3

    def run(self, message, state):

       feedback = None
       best_score = 0
       best_message = message

       for i in range(self.max_iters):

           retrieved_memory = self.memory.search(message.text)

           plan = self.orchestrator.planner.plan(
               message,
               feedback,
               state,
               retrieved=retrieved_memory
            )

           message = self.orchestrator.run_with_plan(message, state, plan)

           if message is None:
               return None

           evaluation = self.evaluator.evaluate(message, state)
           score = evaluation.get("score", 0)

           trace = {
               "input": message.text,
               "strategy": plan["plan"],
               "retrieved": retrieved_memory,
               "state": state.global_meta.copy(),
               "output": message.text,
               "score": score
            }

           if score > 0.6:
                self.memory.store_trace(trace)

           if score > best_score:
               best_score = score
               best_message = message
               state.global_meta["last_score"] = score

           if score > 0.75:
               break

           feedback = evaluation
           message.text = self.rewrite(message.text)

       return best_message