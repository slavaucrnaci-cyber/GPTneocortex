from neocortex_clean.src.blocks.sensory_worker import sensory
from neocortex_clean.src.blocks.shadow_worker import shadow
from neocortex_clean.src.blocks.synthesis_worker import synthesis


def run_pipeline(message, state):
    message = sensory(message, state)
    message = shadow(message, state)
    message = synthesis(message, state)

    return message