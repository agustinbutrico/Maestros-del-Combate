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
