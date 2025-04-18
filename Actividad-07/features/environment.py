from src.belly import Belly
from unittest.mock import MagicMock

def before_scenario(context, scenario):
    # clock mockeado
    fake_clock = MagicMock()
    context.belly = Belly(clock_service=fake_clock)
    context.exception = None