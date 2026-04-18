from src.core.registry import WorkerRegistry
from src.blocks.sensory_worker import SensoryWorker
from src.blocks.shadow_worker import ShadowWorker
from src.blocks.synthesis_worker import SynthesisWorker
from src.blocks.cognitive_worker import CognitiveWorker
from src.core.planner import LLMPlanner


class Orchestrator:

    def __init__(self):
        self.registry = WorkerRegistry()
        self.planner = LLMPlanner()

        # регистрация воркеров
        self.registry.register(SensoryWorker())
        self.registry.register(ShadowWorker())
        self.registry.register(SynthesisWorker())
        self.registry.register(CognitiveWorker())  # 🔥 здесь правильно

    def run_with_plan(self, message, state, plan):
        for step in plan["plan"]:
            print(f"\n→ Running: {step}")

            worker = self.registry.get(step)

            if not worker:
                print(f"⚠️ No worker: {step}")
                continue

            # 💥 считаем попытки shadow
            if step == "shadow":
                state.global_meta["shadow_attempts"] = state.global_meta.get("shadow_attempts", 0) + 1

            result = worker.run(message, state)

            if result is None:
                print(f"💥 ERROR: {step} returned None — STOPPING")
                return message

            message = result

        return message