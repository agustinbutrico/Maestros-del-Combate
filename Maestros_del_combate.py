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

    new_position = None

    while not gs.game_over:
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
                            gs.message_flags["hospital_used"] = True

                    # GYMS FIGHTS >
                    # Water Gym
                    resultado = core.battle.handle_gym_battle(player.pokemons[0], water_gym, water_misty.pokemons[0], "water_completed", "Cerulean Water", (6, 12), 1, 3)
                    if resultado == "win":
                        gs.message_flags["victory_shown"] = True
                    elif resultado == "lose":
                        gs.message_flags["defeat_shown"] = True
                    elif resultado == "exit":
                        gs.game_over = True
                    
                    # Rock Gym
                    resultado = core.battle.handle_gym_battle(player.pokemons[0], rock_gym, rock_brock.pokemons[0], "rock_completed", "Pewter Rock", (7, 13), 1, 3)
                    if resultado == "win":
                        gs.message_flags["victory_shown"] = True
                    elif resultado == "lose":
                        gs.message_flags["defeat_shown"] = True
                    elif resultado == "exit":
                        gs.game_over = True

                    # Electric Gym
                    resultado = core.battle.handle_gym_battle(player.pokemons[0], electric_gym, electric_lt_surge.pokemons[0], "electric_completed", "Vermilion Electric", (8, 14), 2, 3)
                    if resultado == "win":
                        gs.message_flags["victory_shown"] = True
                    elif resultado == "lose":
                        gs.message_flags["defeat_shown"] = True
                    elif resultado == "exit":
                        gs.game_over = True

                    # Fighting Gym
                    resultado = core.battle.handle_gym_battle(player.pokemons[0], fighting_gym, fighting_sabrina.pokemons[0], "fighting_completed", "Cianwood Fighting", (10, 16), 2, 3)
                    if resultado == "win":
                        gs.message_flags["victory_shown"] = True
                    elif resultado == "lose":
                        gs.message_flags["defeat_shown"] = True
                    elif resultado == "exit":
                        gs.game_over = True

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
        if gs.message_flags["hospital_used"]: # Hospital
            player.pokemons[0].hp = player.pokemons[0].max_hp
            print(); core.utils.limpiar_pantalla()
            print(f"{player.pokemons[0].name}'s HP Restored\n\nMove to Continue\n")
            gs.message_flags["hospital_used"] = False

        if gs.message_flags["victory_shown"]: # Gym win
            core.utils.limpiar_pantalla()
            print(
                f"{player.pokemons[0].name} grew to LVL {player.pokemons[0].level - 2}!\n"
                f"{player.pokemons[0].name} grew to LVL {player.pokemons[0].level - 1}!\n"
                f"{player.pokemons[0].name} grew to LVL {player.pokemons[0].level}!\n\n"
                "Gym Cleared\n\nMove to Continue\n"
            )
            gs.message_flags["victory_shown"] = False

        if gs.message_flags["defeat_shown"]: # Gym lost
            core.utils.limpiar_pantalla()
            print("Gym Fight Losed\n\nYou Lose\n")
            gs.game_over = True

        if (gs.gym_flags["rock_completed"] and gs.gym_flags["water_completed"] and 
            gs.gym_flags["electric_completed"] and gs.gym_flags["fighting_completed"]):
            core.utils.limpiar_pantalla()
            print("Congratulations! You win all battles!\n\nYou Win!\n")
            gs.game_over = True
        # < CONDITIONS

        if not gs.game_over and not gs.message_flags["defeat_shown"]:
            direction = readchar() # where player want to move
            new_position = None

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
                gs.game_over = True

            if new_position: # in-game movement
                if gs.obstacles[new_position[POS_Y]][new_position[POS_X]] != ",":
                    gs.user_position = new_position
    # End
