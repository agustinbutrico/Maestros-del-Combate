import os, random
import data.game_state as gs
from time import sleep

def limpiar_pantalla():
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Linux, macOS, etc.
        os.system('clear')

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
        my_position = None

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
                    random.randint(0, gs.MAP_WIDTH - 1), random.randint(0, round(gs.MAP_HEIGHT - ((gs.MAP_HEIGHT - 1) / 1.5))),
                ]
            case "2":
                my_position = [
                    random.randint(0, gs.MAP_WIDTH - 1), random.randint(round((gs.MAP_HEIGHT + 1) / 1.5), gs.MAP_HEIGHT - 1),
                ]
            case "3":
                my_position = [
                    random.randint(round((gs.MAP_WIDTH + 1) / 1.5), gs.MAP_WIDTH - 1), random.randint(0, gs.MAP_HEIGHT - 1),
                ]
            case "4":
                my_position = [
                    random.randint(0, round(gs.MAP_WIDTH - ((gs.MAP_WIDTH - 1) / 1.5))), random.randint(0, gs.MAP_HEIGHT - 1),
                ]
        if my_position is not None:
            gs.user_position = my_position

def time_battle_end(): # time
    sleep(2)