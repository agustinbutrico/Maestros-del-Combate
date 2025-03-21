import random

nuzzle = {
    "type_": "Electrico",
    "damage": 24,
    "accuracy": 0.95,
    "critical_chance": 0.33,
    "critical_multiplier": (random.randint(14, 20))/10,
}

thunder_shock = {
    "type_": "Electrico",
    "damage": 48,
    "accuracy": 0.65,
    "critical_chance": 0.18,
    "critical_multiplier": (random.randint(14, 20))/10,
}

thunder = {
    "type_": "Electrico",
    "damage": 90,
    "accuracy": 0.70,
    "critical_chance": 0.14,
    "critical_multiplier": (random.randint(11, 12))/10,
}

zap_cannon = {
    "type_": "Electrico",
    "damage": 100,
    "accuracy": 0.50,
    "critical_chance": 0.10,
    "critical_multiplier": (random.randint(11, 12))/10,
}
