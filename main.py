from src.core.state import AgentState
from src.core.message import Message
from src.core.agent import Agent


def main():
    state = AgentState()
    agent = Agent()

    message = Message("I feel fear but nothing helps and I am stuck")

    result = agent.run(message, state)

    print("\nFINAL:", result.text)
    print("\n--- TRACE ---")
    for step in result.trace:
        print(step)


if __name__ == "__main__":
    main()