from src.core.state import AgentState
from src.core.message import Message
from src.core.agent import Agent
from src.core.memory import Memory
from src.core.agent import Agent


def main():
    memory = Memory()
    agent = Agent(memory)

    message = Message("I feel fear but nothing helps and I am stuck")

    state = AgentState()   # ← ВОТ ЭТОЙ СТРОКИ НЕ ХВАТАЛ

    result = agent.run(message, state)

    print("\nFINAL:", result.text)
    print("\n--- TRACE ---")
    for step in result.trace:
        print(step)


if __name__ == "__main__":
    main()