class Evaluator:

    def evaluate(self, message, state):
        text = message.text.lower()

        signals = [
            "i can",
            "i choose",
            "i observe",
            "i am able",
            "i will",
        ]

        score = 0.3

        if "fear" in text:
            score -= 0.1

        if any(signal in text for signal in signals):
            score += 0.4

        if "action" in text or "step" in text:
            score += 0.2

        # 🔥 ограничим максимум
        score = min(score, 1.0)

        # 🔥 reason зависит от уровня score
        if score > 0.7:
            reason = "cognitive reframing detected"
        elif score > 0.5:
            reason = "partial reframing"
        else:
            reason = "needs emotional processing"

        return {
            "score": score,
            "ok": score > 0.75,
            "reason": reason
        }