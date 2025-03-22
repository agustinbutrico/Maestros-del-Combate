import random
from time import sleep
from readchar import readchar

from data.load_data import load_data
import data.game_state as gs
import core.battle, core.map, core.utils

POS_X = 0
POS_Y = 1 

def get_trainer_by_name(name):
    """
    Busca y devuelve el entrenador cuyo nombre coincida (sin distinción de mayúsculas/minúsculas)
    en la lista 'trainers'. Si no se encuentra, retorna None.
    """
    for trainer in gs.trainers:
        if trainer.name.lower() == name.lower():
            return trainer
    return None

def time_battle_end(): # time
    sleep(2)

def battle(player_pokemon, enemy_pokemon, gym_name):
    """
    Función de batalla general para enfrentar dos pokémons.
    Retorna:
      - "win" si el jugador gana,
      - "lose" si el jugador pierde,
      - "exit" si el jugador decide salir.
    """
    print()
    core.utils.limpiar_pantalla()
    input(f"You entered -{gym_name} Gym-\n\n")
    core.utils.limpiar_pantalla()

    while True:
        # Turno del jugador
        if player_pokemon.hp > 0:
            my_turn = None
            while my_turn not in ["1", "2", "3", "4", "exit"]:
                core.utils.message_battle_starts(player_pokemon, enemy_pokemon)
                my_turn = input(core.utils.message_pokemon_attacks(player_pokemon))
                core.utils.limpiar_pantalla()

            if my_turn == "exit":
                return "exit"

            attack_index = int(my_turn) - 1
            core.battle.damages(player_pokemon, player_pokemon.attacks[attack_index], enemy_pokemon)
            time_battle_end()
            core.utils.limpiar_pantalla()
        else:
            return "lose"

        # Verificar si el enemigo ha sido derrotado
        if enemy_pokemon.hp < 1:
            return "win"

        # Turno del enemigo
        if enemy_pokemon.hp > 0:
            enemy_attack = random.randint(1, 4)
            core.battle.damages(enemy_pokemon, enemy_pokemon.attacks[enemy_attack - 1], player_pokemon)
            time_battle_end()
            core.utils.limpiar_pantalla()

        # Verificar si el jugador ha sido derrotado
        if player_pokemon.hp < 1:
            return "lose"

if __name__ == '__main__':
    core.utils.limpiar_pantalla()
    load_data()

    player = gs.user
    rock_brock = get_trainer_by_name("Brock")
    water_misty = get_trainer_by_name("Misty")
    electric_lt_surge = get_trainer_by_name("Lt. Surge")
    fighting_sabrina = get_trainer_by_name("Sabrina")

    core.utils.intro(player.pokemons[0])

    # Extraer las ubicaciones usando atributos semánticos
    rock_gym     = next(g for g in gs.gyms if g.type_ == "Roca")
    water_gym    = next(g for g in gs.gyms if g.type_ == "Agua")
    electric_gym = next(g for g in gs.gyms if g.type_ == "Electrico")
    fighting_gym = next(g for g in gs.gyms if g.type_ == "Lucha")
    # Para los hospitales, suponiendo que se les asigna un id autoincremental:
    hospital_1   = next(h for h in gs.hospitals if h.id == 1)
    hospital_2   = next(h for h in gs.hospitals if h.id == 2)

    rock_done = False
    water_done = False
    electric_done = False
    fighting_done = False
    locations_true = False
    game_true = False
    true_1 = False
    true_2 = False
    true_3 = False
    playing = True
    new_position = None

    while not game_true:
        core.utils.limpiar_pantalla()
        # DIBUJO DEL MAPA >
        print("-"*(gs.MAP_WIDTH* 2 + 3)) # Top

        for coordinate_y in range(gs.MAP_HEIGHT):
            print("|", end="") # Lado izquierdo

            for coordinate_x in range(gs.MAP_WIDTH):
                char_to_draw = "  " # Inicialmente, se asume un espacio vacío

                # Se busca en gs.locations si hay alguna ubicación en la posición actual
                location = next((l for l in gs.locations if l.x == coordinate_x and l.y == coordinate_y), None)
                if location is not None:
                    char_to_draw = location.icon

                # YOU >
                if gs.user_position[POS_X] == coordinate_x and gs.user_position[POS_Y] == coordinate_y: # tu posición
                    char_to_draw = " @" # you

                    for hospital in gs.hospitals:
                        if hospital.x == coordinate_x and hospital.y == coordinate_y:
                            # En el futuro se diferenciará entre hospitales
                            if hospital.id == 1:
                                true_1 = True
                            elif hospital.id == 2:
                                true_1 = True

                    # GYMS FIGHTS >
                    # Water Gym
                    if water_gym.x == coordinate_x and water_gym.y == coordinate_y and not water_done:
                        resultado = battle(player.pokemons[0], water_misty.pokemons[0], "Cerulean Water")
                        if resultado == "win":
                            player.pokemons[0].max_hp += random.randint(6, 12)
                            player.pokemons[0].damage += 1
                            player.pokemons[0].level += 3
                            water_done = True
                            true_2 = True
                        elif resultado == "lose":
                            true_3 = True
                            water_done = True
                        elif resultado == "exit":
                            game_true = True
                            water_done = True
                            playing = False
                    
                    # Rock Gym
                    if rock_gym.x == coordinate_x and rock_gym.y == coordinate_y and not rock_done:
                        resultado = battle(player.pokemons[0], rock_brock.pokemons[0], "Pewter Rock")
                        if resultado == "win":
                            player.pokemons[0].max_hp += random.randint(7, 13)
                            player.pokemons[0].damage += 1
                            player.pokemons[0].level += 3
                            rock_done = True
                            true_2 = True
                        elif resultado == "lose":
                            true_3 = True
                            rock_done = True
                        elif resultado == "exit":
                            game_true = True
                            rock_done = True
                            playing = False

                    # Electric Gym
                    if electric_gym.x == coordinate_x and electric_gym.y == coordinate_y and not electric_done:
                        resultado = battle(player.pokemons[0], electric_lt_surge.pokemons[0], "Vermilion Electric")
                        if resultado == "win":
                            player.pokemons[0].max_hp += random.randint(8, 14)
                            player.pokemons[0].damage += 2
                            player.pokemons[0].level += 3
                            electric_done = True
                            true_2 = True
                        elif resultado == "lose":
                            true_3 = True
                            electric_done = True
                        elif resultado == "exit":
                            game_true = True
                            electric_done = True
                            playing = False

                    # Fighting Gym
                    if fighting_gym.x == coordinate_x and fighting_gym.y == coordinate_y and not fighting_done:
                        resultado = battle(player.pokemons[0], fighting_sabrina.pokemons[0], "Cianwood Fighting")
                        if resultado == "win":
                            player.pokemons[0].max_hp += random.randint(10, 16)
                            player.pokemons[0].damage += 2
                            player.pokemons[0].level += 3
                            fighting_done = True
                            true_2 = True
                        elif resultado == "lose":
                            true_3 = True
                            fighting_done = True
                        elif resultado == "exit":
                            game_true = True
                            fighting_done = True
                            playing = False  

                    # < GYMS FIGHTS
                # < YOU

                # WALLS PRINT >
                if gs.obstacles[coordinate_y][coordinate_x] == ",": # Walls
                    if gs.obstacles[gs.user_position[POS_Y]][gs.user_position[POS_X]] == ",": # don't draw walls on you
                        gs.obstacles[gs.user_position[POS_Y]][gs.user_position[POS_X]] = " "
                    if gs.obstacles[gs.user_position[POS_Y]][gs.user_position[POS_X]] != ",": # walls print
                        char_to_draw = " #"
                # < WALLS PRINT

                print("{}".format(char_to_draw), end="") # Printer
            print(" |") # Lado derecho

        print("-"*(gs.MAP_WIDTH* 2 + 3)) # Bottom
        # < DRAW MAP

        # CONDITIONS >
        if true_1: # Hospital
            player.pokemons[0].hp = player.pokemons[0].max_hp
            print(); core.utils.limpiar_pantalla()
            print(f"{player.pokemons[0].name}'s HP Restored\n\nMove to Continue\n")
            true_1 = False
        if true_2: # Gym win
            core.utils.limpiar_pantalla(); print(f"{player.pokemons[0].name} grew to LVL {player.pokemons[0].level - 2}!\n"
                                f"{player.pokemons[0].name} grew to LVL {player.pokemons[0].level - 1}!\n"
                                f"{player.pokemons[0].name} grew to LVL {player.pokemons[0].level}!\n\n"
                                "Gym Cleared\n\nMove to Continue\n")
            true_2 = False
        if true_3: # Gym lost
            core.utils.limpiar_pantalla(); print("Gym Fight Losed\n\nYou Lose\n")
            game_true = True
        if rock_done and water_done and electric_done and fighting_done: # win conditions
            core.utils.limpiar_pantalla(); print("Congratulations! You win all battles!\n\nYou Win!\n")
            game_true = True
        if not playing: # exit game
            print(); core.utils.limpiar_pantalla()
        # < CONDITIONS

        if not game_true and not true_3:
            direction = readchar() # where player want to move

            if direction.upper() == "W": # up movement
                new_position = [gs.user_position[POS_X], gs.user_position[POS_Y] - 1]
                if new_position[POS_Y] < 0:
                    new_position[POS_Y] = gs.MAP_HEIGHT - 1

            elif direction.upper() == "S": # down movement
                new_position = [gs.user_position[POS_X], gs.user_position[POS_Y] + 1]
                if new_position[POS_Y] > gs.MAP_HEIGHT - 1:
                    new_position[POS_Y] = 0

            elif direction.upper() == "A": # left movement
                new_position = [gs.user_position[POS_X] - 1, gs.user_position[POS_Y]]
                if new_position[POS_X] < 0:
                    new_position[POS_X] = gs.MAP_WIDTH - 1

            elif direction.upper() == "D": # right movement
                new_position = [gs.user_position[POS_X] + 1, gs.user_position[POS_Y]]
                if new_position[POS_X] > gs.MAP_WIDTH - 1:
                    new_position[POS_X] = 0

            elif direction.upper() == "P": # right movement
                game_true = True

            if new_position: # in-game movement
                if gs.obstacles[new_position[POS_Y]][new_position[POS_X]] != ",":
                    gs.user_position = new_position
    # End