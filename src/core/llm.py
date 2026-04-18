def call_llm(prompt: str) -> str:
    prompt_lower = prompt.lower()

    # если это planner
    if "ai system planner" in prompt_lower:

        if "fear" in prompt_lower or "uncertainty" in prompt_lower:
            return '{"plan": ["sensory", "shadow", "synthesis"]}'
        else:
            return '{"plan": ["sensory", "synthesis"]}'

    # если это synthesis
    return f"[LLM RESPONSE]: {prompt}"