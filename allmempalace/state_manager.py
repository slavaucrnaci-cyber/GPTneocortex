def update_pattern(self, name, confidence, trend=None, trigger=None):
        print("UPDATE CALLED:", name, confidence)
        from datetime import datetime
        # ❗ фильтр
        if confidence < 0.55:
            print("SKIPPED (low confidence):", name, confidence)
            return

        # Получаем текущий паттерн или создаем пустой словарь
        pattern = self.state["patterns"].get(name, {})

        old_conf = pattern.get("confidence", confidence)
        old_vol = pattern.get("volatility", 0)

        # 🔥 confidence (инерция)
        new_conf = (old_conf * 0.7) + (confidence * 0.3)

        # 🔥 volatility
        raw_vol = abs(new_conf - old_conf)
        new_vol = (old_vol * 0.7) + (raw_vol * 0.3)

        # 🔥 тренд
        if new_conf > old_conf:
            new_trend = "increasing"
        elif new_conf < old_conf:
            new_trend = "decreasing"
        else:
            new_trend = "stable"

        pattern.update({
            "confidence": round(new_conf, 3),
            "trend": new_trend,
            "volatility": round(new_vol, 3),
            "last_trigger": trigger,
            "last_updated": datetime.now().isoformat()
        })

        self.state["patterns"][name] = pattern  # Исправлено с elf на self
        self.save_state()
        
        # Внутри state_manager.py
from .dialect import Dialect

class IntegratedStateManager(StateManager):
 def analyze_and_update(self, text):
        """
        Анализирует текст через AAAK Dialect и обновляет паттерны.
        """
        dialect = Dialect()
        # Извлекаем эмоции через ваш диалект AAAK
        compressed = dialect.compress(text)
        
        # Простая логика маппинга эмоций на паттерны
        if "anx" in compressed or "fear" in compressed:
            self.update_pattern("anxiety_level", 0.75, trigger="text_analysis")
        
        if "raw" in compressed or "convict" in compressed:
            self.update_pattern("ego_strength", 0.80, trigger="insight")
            
        return compressed