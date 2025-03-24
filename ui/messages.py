import core.utils as cu
import data.game_state as gs

def message_fight_entry(gym, entry_message=None):
    """
    Muestra el mensaje de entrada al gimnasio. 
    Permite pasar un mensaje personalizado por parámetro.
    """
    cu.limpiar_pantalla()
    message = entry_message if entry_message else f"You entered -{gym.alias} Gym-\n\n"
    input(message)

def message_battle_starts(trainer):
    user_pokemon = gs.user.pokemons[0]
    enemy_pokemon = trainer.pokemons[0]

    message = (
        f"{enemy_pokemon.name} {enemy_pokemon.hp} HP\n"
        f"{cu.message_life_indicator(enemy_pokemon)}\n\n"
        f"{user_pokemon.name} {user_pokemon.hp} HP\n"
        f"{cu.message_life_indicator(user_pokemon)}\n\n"
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

    message = "Select your attack:\n\n"
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
    message = (
         f"{enemy.name} {enemy.hp} HP\n"
         f"{cu.message_life_indicator(enemy)}\n\n"
         f"{attacker.name} uses {attack.name}\n"
    )

    if gs.battle_flags["move_normal"]:
            message += f"Normal hit -{damage_dealt}\n"
    elif gs.battle_flags["move_critic"]:
            message += f"Critical hit! -{damage_dealt}\n"
    elif gs.battle_flags["move_miss"]:
        message += "Miss___\n"
    message += ("\n")

    cu.limpiar_pantalla()
    print(message)
