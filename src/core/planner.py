class LLMPlanner:

    def plan(self, message, feedback=None, state=None):
        text = message.text.lower()

        score = 0
        if state:
            score = state.global_meta.get("last_score", 0)

        # 💥 если решение слабое — меняем стратегию
        if score < 0.5 and feedback:

            shadow_attempts = state.global_meta.get("shadow_attempts", 0)

            if shadow_attempts >= 2:
                return {
                    "plan": ["sensory", "cognitive", "synthesis"]
                }

            return {
                "plan": ["sensory", "shadow", "shadow", "synthesis"]
            }

        # 💥 если уже хорошо — не усложняем
        if score > 0.7:
            return {
                "plan": ["sensory", "synthesis"]
            }

        # базовая логика
        if "fear" in text or "uncertainty" in text:
            return {
                "plan": ["sensory", "shadow", "synthesis"]
            }

        return {
            "plan": ["sensory", "synthesis"]
        }