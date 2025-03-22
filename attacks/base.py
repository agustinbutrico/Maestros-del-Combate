import attacks

class Attack:
    def __init__(self, name, type_, damage, accuracy, critical_chance, critical_multiplier):
        self.name = name
        self.type_ = type_
        self.damage = damage
        self.accuracy = accuracy
        self.critical_chance = critical_chance
        self.critical_multiplier = critical_multiplier

    def is_compatible_with(self, pokemon_types):
        return self.type_ in pokemon_types or self.type_ == "Normal"

    def __repr__(self):
        return f"<Ataque {self.name} ({self.type_})>"
    
class AttacksFactory:
    _attacks_data = {
        "Nuzzle": attacks.electric.nuzzle,
        "Thunder shock": attacks.electric.thunder_shock,
        "Quick attack": attacks.normal.quick_attack,
        "Feint": attacks.normal.feint,
        "Tackle": attacks.normal.tackle,
        "Water gun": attacks.water.water_gun,
        "Rapid spin": attacks.normal.rapid_spin,
        "Bite": attacks.dark.bite,
        "Water pulse": attacks.water.water_pulse,
        "Metal claw": attacks.steel.metal_claw,
        "Rock tomb": attacks.rock.rock_tomb,
        "Headbutt": attacks.normal.headbutt,
        "Rock slide": attacks.rock.rock_slide,
        "Iron tail": attacks.steel.iron_tail,
        "Peck": attacks.flying.peck,
        "Pluck": attacks.flying.pluck,
        "Ancient power": attacks.rock.ancient_power,
        "Thunder": attacks.electric.thunder,
        "Zap cannon": attacks.electric.zap_cannon,
        "Drain punch": attacks.fighting.drain_punch,
        "Power-up punch": attacks.fighting.power_up_punch,
        "Fire punch": attacks.fire.fire_punch,
        "Mega punch": attacks.normal.mega_punch,
        "Focus punch": attacks.fighting.focus_punch,
    }

    @staticmethod
    def create_attack(name):
        if name not in AttacksFactory._attacks_data:
            raise ValueError(f"No hay datos para el ataque '{name}'.")
        
        data = AttacksFactory._attacks_data[name]
        return Attack(name=name, **data)
