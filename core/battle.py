import random
import core.utils

def damages(attacker, attack, enemy):
    """
    Realiza un ataque de 'attacker' usando el objeto 'attack' contra 'enemy',
    calculando y aplicando el daño de forma crítica o normal.
    """
    print(f"{attacker.name} uses {attack.name}\n")
    
    if random.random() < attack.accuracy:
        if random.random() < attack.critical_chance:
            damage_dealt = int(attack.damage * attack.critical_multiplier)
            print(f"Critical hit! -{damage_dealt}\n")
        else:
            damage_dealt = attack.damage
            print(f"-{damage_dealt}\n")
        enemy.hp -= damage_dealt
    else:
        print("Miss___\n")
        
    print(f"{enemy.name} {enemy.hp} HP\n{core.utils.message_life_indicator(enemy)}\n")
