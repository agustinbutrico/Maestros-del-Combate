import random

rock_tomb = {
    "type_": "Rock",
    "damage": 60,
    "accuracy": 0.95,
    "critical_chance": 0.20,
    "critical_multiplier": (random.randint(11, 14))/10,
}

rock_slide = {
    "type_": "Rock",
    "damage": 75,
    "accuracy": 0.90,
    "critical_chance": 0.18,
    "critical_multiplier": (random.randint(11, 14))/10,
}

ancient_power = {
    "type_": "Rock",
    "damage": 60,
    "accuracy": 1.00,
    "critical_chance": 0.20,
    "critical_multiplier": (random.randint(11, 12))/10,
}
