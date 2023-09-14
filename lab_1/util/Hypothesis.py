from typing import Callable


class Hypothesis:
    h0: str
    h1: str
    condition: Callable[[float], str]

    def __init__(self, h0: str, h1: str, condition: Callable[[float], str]):
        self.h0 = h0
        self.h1 = h1
        self.condition = condition

    def compute(self, value: float) -> str:
        if self.condition(value):
            return self.h0.format(val=value)
        else:
            return self.h1.format(val=value)
