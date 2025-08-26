import random

class Dice:
    """Lógica de tiradas de dos dados."""
    def roll(self):
        d1, d2 = random.randint(1,6), random.randint(1,6)
        return [d1, d2] * (2 if d1 == d2 else 1)
