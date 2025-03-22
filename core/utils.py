import os, random
from data.game_state import MAP_HEIGHT, MAP_WIDTH

def limpiar_pantalla():
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Linux, macOS, etc.
        os.system('clear')

def message_pokemon_attacks(pokemon):
    """
    Devuelve un mensaje con la lista de ataques del Pokémon,
    mostrando el número, nombre, daño, precisión y probabilidad crítica.
    """
    message = "Select your attack:\n\n"
    for index, attack in enumerate(pokemon.attacks, start=1):
        message += (
            f"{index}. {attack.name}\n"
            f"    {attack.damage} damage\n"
            f"    {round(attack.accuracy * 100)}% accuracy\n"
            f"    {round(attack.critical_chance * 100)}% critical chance\n\n"
        )
    return message

def message_battle_starts(attacker, enemy):
    print(
        f"{enemy.name} {enemy.hp} HP\n{message_life_indicator(enemy)}\n\n"
        f"{attacker.name} {attacker.hp} HP\n{message_life_indicator(attacker)}\n\n"
        f"{attacker.name}'s LVL {attacker.level}\n\n"
        f"{attacker.name}'s Damage: {attacker.damage}\n\n"
    )

def message_life_indicator(pokemon): # Health Bar
    """Retorna una barra de vida en formato texto basada en hp y max_hp."""
    if pokemon.hp >= 0:
        health_bar = int(pokemon.hp * 30 / pokemon.max_hp)
        health_bar_print = "[{}{}]".format("#" * health_bar, " " *(30 - health_bar))
    elif pokemon.hp < 0:
        health_bar = int(-1 *(pokemon.hp * 30 / pokemon.max_hp))
        health_bar_print = "[{}{}]".format(" " *(30 - health_bar), "/" * health_bar)
    return health_bar_print

def intro(pokemon):
    location = ""
    while location not in ["1", "2", "3", "4"]:
        print(
            f"(i) Hospitals [H] restores HP\n"
            f"(i) WASD to move\n\n"
            f"{pokemon.name} {pokemon.hp} HP            LVL {pokemon.level}\n"
            f"{message_life_indicator(pokemon)}\n"
        )

        # Listamos los ataques dinámicamente
        print(f"{pokemon.name} knows the following movements:")
        for attack in pokemon.attacks:
            print(f"  - {attack.name}")

        location = input(
            "Where are you coming from:\n  North (1)\n  South (2)\n  East  (3)\n  West  (4)\n\n"
        )
        limpiar_pantalla()

        match location:
            case "1":
                my_position = [
                    random.randint(0, MAP_WIDTH - 1), random.randint(0, round(MAP_HEIGHT - ((MAP_HEIGHT - 1) / 1.5))),
                ]
            case "2":
                my_position = [
                    random.randint(0, MAP_WIDTH - 1), random.randint(round((MAP_HEIGHT + 1) / 1.5), MAP_HEIGHT - 1),
                ]
            case "3":
                my_position = [
                    random.randint(round((MAP_WIDTH + 1) / 1.5), MAP_WIDTH - 1), random.randint(0, MAP_HEIGHT - 1),
                ]
            case "4":
                my_position = [
                    random.randint(0, round(MAP_WIDTH - ((MAP_WIDTH - 1) / 1.5))), random.randint(0, MAP_HEIGHT - 1),
                ]
    return my_position