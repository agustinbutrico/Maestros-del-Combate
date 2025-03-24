import core.utils as cu
import data.game_state as gs

def message_info_intro(trainer):
    trainer_pokemon = trainer.pokemons[0]
    
    message = (
        f"(i) HP can be restored in Hospitals [H]\n"
        f"(i) WASD to move\n\n"
        f"You have a {trainer_pokemon.name}\n"
        f"HP: {trainer_pokemon.hp}   "
        f"LVL: {trainer_pokemon.level}\n"
    )

    return message

def message_start_location_selection():
    cu.limpiar_pantalla()
    locations = [ "North", "South", "East", "West" ]

    message = "Where are you from:\n"
    for index, location in enumerate(locations, start=1):
        message += (
            f"{index}. {location}\n"
        )
    
    return message

def message_fight_entry(gym, entry_message=None):
    """
    Muestra el mensaje de entrada al gimnasio. 
    Permite pasar un mensaje personalizado por parámetro.
    """
    cu.limpiar_pantalla()
    message = entry_message if entry_message else f"You entered -{gym.alias} Gym-\n\n"

    return message

def message_battle_starts(enemy):
    user_pokemon = gs.user.pokemons[0]
    enemy_pokemon = enemy.pokemons[0]

    message = (
        f"{enemy_pokemon.name} {enemy_pokemon.hp} HP\n"
        f"{message_life_indicator(enemy)}\n\n"
        f"{user_pokemon.name} {user_pokemon.hp} HP\n"
        f"{message_life_indicator(gs.user)}\n\n"
        f"{user_pokemon.name}'s LVL {user_pokemon.level}\n\n"
        f"{user_pokemon.name}'s Damage: {user_pokemon.damage}\n\n"
    )

    return message

def message_pokemon_attacks(trainer):
    """
    Devuelve un mensaje con la lista de ataques del Pokémon,
    mostrando el número, nombre, daño, precisión y probabilidad crítica.
    """
    trainer_pokemon = trainer.pokemons[0]

    message = "Attacks:\n"
    for attack in trainer_pokemon.attacks:
        message += (
            f" - {attack.name}\n"
        )

    return message

def message_pokemon_attacks_detailed(trainer):
    """
    Devuelve un mensaje con la lista de ataques del Pokémon,
    mostrando el número, nombre, daño, precisión y probabilidad crítica.
    """
    trainer_pokemon = trainer.pokemons[0]

    message = "Attacks:\n"
    for index, attack in enumerate(trainer_pokemon.attacks, start=1):
        message += (
            f"{index}. {attack.name}\n"
            f"    {attack.damage} damage\n"
            f"    {round(attack.accuracy * 100)}% accuracy\n"
            f"    {round(attack.critical_chance * 100)}% critical chance\n\n"
        )

    return message

def message_attack_damage(attacker, attack, enemy, damage_dealt):
    """
    Retorna una lista de mensajes sobre lo ocurrido (ataque crítico, daño, etc.).
    Se hace uso de las flags definidas en battle_flags
      - "move_normal" si el daño del movimiento fue normal,
      - "move_critic" si el daño del movimiento fue critico,
      - "move_miss" si el daño del movimiento fue nulo,
    """
    cu.limpiar_pantalla()
    attacker_pokemon = attacker.pokemons[0]
    enemy_pokemon = enemy.pokemons[0]

    message = (
         f"{enemy_pokemon.name} {enemy_pokemon.hp} HP\n"
         f"{message_life_indicator(enemy)}\n\n"
         f"{attacker_pokemon.name} uses {attack.name}\n"
    )

    if gs.battle_flags["move_normal"]:
            message += f"Normal hit -{damage_dealt}\n"
    elif gs.battle_flags["move_critic"]:
            message += f"Critical hit! -{damage_dealt}\n"
    elif gs.battle_flags["move_miss"]:
        message += "Miss___\n"
    message += ("\n")

    return message

def message_life_indicator(trainer): # Health Bar
    """Retorna una barra de vida en formato texto basada en hp y max_hp."""
    trainer_pokemon = trainer.pokemons[0]

    if trainer_pokemon.hp >= 0:
        health_bar = int(trainer_pokemon.hp * 30 / trainer_pokemon.max_hp)
        health_bar_print = "[{}{}]".format("#" * health_bar, " " *(30 - health_bar))
    elif trainer_pokemon.hp < 0:
        health_bar = int(-1 *(trainer_pokemon.hp * 30 / trainer_pokemon.max_hp))
        health_bar_print = "[{}{}]".format(" " *(30 - health_bar), "/" * health_bar)

    return health_bar_print