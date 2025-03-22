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
                    if not water_done: # Water Gym

                        if water_gym.x == coordinate_x and water_gym.y == coordinate_y:
                            print(); core.utils.limpiar_pantalla(); input("You entered -Cerulean Water Gym-\n\n"); core.utils.limpiar_pantalla()

                            while not water_done: # water gym fight

                                if player.pokemons[0].hp > 0:
                                    my_turn = None
                                    while my_turn not in ["1", "2", "3", "4", "exit"]:
                                        core.utils.message_battle_starts(player.pokemons[0], water_misty.pokemons[0])
                                        my_turn = input(core.utils.message_pokemon_attacks(player.pokemons[0])); core.utils.limpiar_pantalla()

                                    if my_turn == "1":
                                        core.battle.damages(player.pokemons[0], player.pokemons[0].attacks[0], water_misty.pokemons[0])
                                    elif my_turn == "2":
                                        core.battle.damages(player.pokemons[0], player.pokemons[0].attacks[1], water_misty.pokemons[0])
                                    elif my_turn == "3":
                                        core.battle.damages(player.pokemons[0], player.pokemons[0].attacks[2], water_misty.pokemons[0])
                                    elif my_turn == "4":
                                        core.battle.damages(player.pokemons[0], player.pokemons[0].attacks[3], water_misty.pokemons[0])
                                    elif my_turn == "exit":
                                        game_true = True; water_done = True; playing = False
                                    time_battle_end(); core.utils.limpiar_pantalla()

                                if playing:
                                    if water_misty.pokemons[0].hp > 0:
                                        turn = random.randint(1, 4)

                                        if turn == 1:
                                            core.battle.damages(water_misty.pokemons[0], water_misty.pokemons[0].attacks[0], player.pokemons[0])
                                        elif turn == 2:
                                            core.battle.damages(water_misty.pokemons[0], water_misty.pokemons[0].attacks[1], player.pokemons[0])
                                        elif turn == 3:
                                            core.battle.damages(water_misty.pokemons[0], water_misty.pokemons[0].attacks[2], player.pokemons[0])
                                        elif turn == 4:
                                            core.battle.damages(water_misty.pokemons[0], water_misty.pokemons[0].attacks[3], player.pokemons[0])
                                        time_battle_end(); core.utils.limpiar_pantalla()

                                if water_misty.pokemons[0].hp < 1:
                                    true_2 = True
                                    water_done = True

                                    player.pokemons[0].max_hp += random.randint(6, 12)
                                    player.pokemons[0].damage += 1
                                    player.pokemons[0].level += 3

                                    # pikachu_critical = ((pikachu_critical * 10) + 1)/10
                                    # nuzzle["damage"] = int((pikachu["damage"]) * 2.5)
                                    # thunder_shock["damage"] = int((pikachu["damage"]) * 4.5)
                                    # quick_attack["damage"] = int((pikachu["damage"]) * 4)
                                    # feint["damage"] = int((pikachu["damage"]) * 3)
                                elif player.pokemons[0].hp < 1:
                                    true_3 = True
                                    water_done = True

                    if not rock_done: # Rock Gym

                        if rock_gym.x == coordinate_x and rock_gym.y == coordinate_y:
                            print(); core.utils.limpiar_pantalla(); input("You entered -Pewter Rock Gym-\n\n"); core.utils.limpiar_pantalla()

                            while not rock_done: # rock gym fight

                                if player.pokemons[0].hp > 0:
                                    my_turn = None
                                    while my_turn not in ["1", "2", "3", "4", "exit"]:
                                        core.utils.message_battle_starts(player.pokemons[0], rock_brock.pokemons[0])
                                        my_turn = input(core.utils.message_pokemon_attacks(player.pokemons[0])); core.utils.limpiar_pantalla()

                                    if my_turn == "1":
                                        core.battle.damages(player.pokemons[0], player.pokemons[0].attacks[0], rock_brock.pokemons[0])
                                    elif my_turn == "2":
                                        core.battle.damages(player.pokemons[0], player.pokemons[0].attacks[1], rock_brock.pokemons[0])
                                    elif my_turn == "3":
                                        core.battle.damages(player.pokemons[0], player.pokemons[0].attacks[2], rock_brock.pokemons[0])
                                    elif my_turn == "4":
                                        core.battle.damages(player.pokemons[0], player.pokemons[0].attacks[3], rock_brock.pokemons[0])
                                    elif my_turn == "exit":
                                        game_true = True; rock_done = True; playing = False
                                    time_battle_end(); core.utils.limpiar_pantalla()

                                if playing:
                                    if rock_brock.pokemons[0].hp > 0:
                                        turn = random.randint(1, 4)

                                        if turn == 1:
                                            core.battle.damages(rock_brock.pokemons[0], rock_brock.pokemons[0].attacks[0], player.pokemons[0])
                                        elif turn == 2:
                                            core.battle.damages(rock_brock.pokemons[0], rock_brock.pokemons[0].attacks[1], player.pokemons[0])
                                        elif turn == 3:
                                            core.battle.damages(rock_brock.pokemons[0], rock_brock.pokemons[0].attacks[2], player.pokemons[0])
                                        elif turn == 4:
                                            core.battle.damages(rock_brock.pokemons[0], rock_brock.pokemons[0].attacks[3], player.pokemons[0])
                                        time_battle_end(); core.utils.limpiar_pantalla()

                                if rock_brock.pokemons[0].hp < 1:
                                    true_2 = True
                                    rock_done = True

                                    player.pokemons[0].max_hp += random.randint(7, 13)
                                    player.pokemons[0].damage += 1
                                    player.pokemons[0].level += 3

                                    # pikachu_critical = ((pikachu_critical * 10) + 1)/10
                                    # nuzzle["damage"] = int((pikachu["damage"]) * 2.5)
                                    # thunder_shock["damage"] = int((pikachu["damage"]) * 4.5)
                                    # quick_attack["damage"] = int((pikachu["damage"]) * 4)
                                    # feint["damage"] = int((pikachu["damage"]) * 3)
                                elif player.pokemons[0].hp < 1:
                                    true_3 = True
                                    rock_done = True

                    if not electric_done: # Electric Gym

                        if electric_gym.x == coordinate_x and electric_gym.y == coordinate_y:
                            print(); core.utils.limpiar_pantalla(); input("You entered -Vermilion Electric Gym-\n\n"); core.utils.limpiar_pantalla()

                            while not electric_done: # electric gym fight

                                if player.pokemons[0].hp > 0:
                                    my_turn = None
                                    while my_turn not in ["1", "2", "3", "4", "exit"]:
                                        core.utils.message_battle_starts(player.pokemons[0], electric_lt_surge.pokemons[0])
                                        my_turn = input(core.utils.message_pokemon_attacks(player.pokemons[0])); core.utils.limpiar_pantalla()

                                    if my_turn == "1":
                                        core.battle.damages(player.pokemons[0], player.pokemons[0].attacks[0], electric_lt_surge.pokemons[0])
                                    elif my_turn == "2":
                                        core.battle.damages(player.pokemons[0], player.pokemons[0].attacks[1], electric_lt_surge.pokemons[0])
                                    elif my_turn == "3":
                                        core.battle.damages(player.pokemons[0], player.pokemons[0].attacks[2], electric_lt_surge.pokemons[0])
                                    elif my_turn == "4":
                                        core.battle.damages(player.pokemons[0], player.pokemons[0].attacks[3], electric_lt_surge.pokemons[0])
                                    elif my_turn == "exit":
                                        game_true = True; electric_done = True; playing = False
                                    time_battle_end(); core.utils.limpiar_pantalla()

                                if playing:
                                    if electric_lt_surge.pokemons[0].hp > 0:
                                        turn = random.randint(1, 4)

                                        if turn == 1:
                                            core.battle.damages(electric_lt_surge.pokemons[0], electric_lt_surge.pokemons[0].attacks[0], player.pokemons[0])
                                        elif turn == 2:
                                            core.battle.damages(electric_lt_surge.pokemons[0], electric_lt_surge.pokemons[0].attacks[1], player.pokemons[0])
                                        elif turn == 3:
                                            core.battle.damages(electric_lt_surge.pokemons[0], electric_lt_surge.pokemons[0].attacks[2], player.pokemons[0])
                                        elif turn == 4:
                                            core.battle.damages(electric_lt_surge.pokemons[0], electric_lt_surge.pokemons[0].attacks[3], player.pokemons[0])
                                        time_battle_end(); core.utils.limpiar_pantalla()

                                if electric_lt_surge.pokemons[0].hp < 1:
                                    true_2 = True
                                    electric_done = True

                                    player.pokemons[0].max_hp += random.randint(8, 14)
                                    player.pokemons[0].damage += 2
                                    player.pokemons[0].level += 3

                                    # pikachu_critical = ((pikachu_critical * 10) + 1)/10
                                    # nuzzle["damage"] = int((pikachu["damage"]) * 2.5)
                                    # thunder_shock["damage"] = int((pikachu["damage"]) * 4.5)
                                    # quick_attack["damage"] = int((pikachu["damage"]) * 4)
                                    # feint["damage"] = int((pikachu["damage"]) * 3)
                                elif player.pokemons[0].hp < 1:
                                    true_3 = True
                                    electric_done = True

                    if not fighting_done: # Fighting Gym

                        if fighting_gym.x == coordinate_x and fighting_gym.y == coordinate_y:
                            print(); core.utils.limpiar_pantalla(); input("You entered -Cianwood Fighting Gym\n\n"); core.utils.limpiar_pantalla()

                            while not fighting_done: # fighting gym fight

                                if player.pokemons[0].hp > 0:
                                    my_turn = None
                                    while my_turn not in ["1", "2", "3", "4", "exit"]:
                                        core.utils.message_battle_starts(player.pokemons[0], fighting_sabrina.pokemons[0])
                                        my_turn = input(core.utils.message_pokemon_attacks(player.pokemons[0])); core.utils.limpiar_pantalla()

                                    if my_turn == "1":
                                        core.battle.damages(player.pokemons[0], player.pokemons[0].attacks[0], fighting_sabrina.pokemons[0])
                                    elif my_turn == "2":
                                        core.battle.damages(player.pokemons[0], player.pokemons[0].attacks[1], fighting_sabrina.pokemons[0])
                                    elif my_turn == "3":
                                        core.battle.damages(player.pokemons[0], player.pokemons[0].attacks[2], fighting_sabrina.pokemons[0])
                                    elif my_turn == "4":
                                        core.battle.damages(player.pokemons[0], player.pokemons[0].attacks[3], fighting_sabrina.pokemons[0])
                                    elif my_turn == "exit":
                                        game_true = True; fighting_done = True; playing = False
                                    time_battle_end(); core.utils.limpiar_pantalla()

                                if playing:
                                    if fighting_sabrina.pokemons[0].hp > 0:
                                        turn = random.randint(1, 4)

                                        if turn == 1:
                                            core.battle.damages(fighting_sabrina.pokemons[0], fighting_sabrina.pokemons[0].attacks[0], player.pokemons[0])
                                        elif turn == 2:
                                            core.battle.damages(fighting_sabrina.pokemons[0], fighting_sabrina.pokemons[0].attacks[1], player.pokemons[0])
                                        elif turn == 3:
                                            core.battle.damages(fighting_sabrina.pokemons[0], fighting_sabrina.pokemons[0].attacks[2], player.pokemons[0])
                                        elif turn == 4:
                                            core.battle.damages(fighting_sabrina.pokemons[0], fighting_sabrina.pokemons[0].attacks[3], player.pokemons[0])
                                        time_battle_end(); core.utils.limpiar_pantalla()

                                if fighting_sabrina.pokemons[0].hp < 1:
                                    true_2 = True
                                    fighting_done = True

                                    player.pokemons[0].max_hp += random.randint(10, 16)
                                    player.pokemons[0].damage += 2
                                    player.pokemons[0].level += 3

                                    # pikachu_critical = ((pikachu_critical * 10) + 1)/10
                                    # nuzzle["damage"] = int((pikachu["damage"]) * 2.5)
                                    # thunder_shock["damage"] = int((pikachu["damage"]) * 4.5)
                                    # quick_attack["damage"] = int((pikachu["damage"]) * 4)
                                    # feint["damage"] = int((pikachu["damage"]) * 3)
                                elif player.pokemons[0].hp < 1:
                                    true_3 = True
                                    fighting_done = True
        
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