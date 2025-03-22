import random
import data.game_state as gs
import pokemons.base as pokemons
import attacks.base as attacks

def assign_attacks_to_pokemon(pokemon, num_attacks=4):
    """
    Asigna hasta `num_attacks` ataques compatibles al Pokémon dado.
    
    Parámetros:
      - pokemon: instancia del Pokémon al que se asignarán los ataques.
      - num_attacks (int): cantidad máxima de ataques a asignar (por defecto 4).
      
    Retorna:
      - El mismo objeto pokemon con los ataques asignados.
    """
    # Obtener la lista de nombres de ataques disponibles
    available_attacks = list(attacks.AttacksFactory._attacks_data.keys())
    compatible_attacks = []
    
    # Filtrar los ataques compatibles con los tipos del Pokémon
    for attack_name in available_attacks:
        try:
            attack = attacks.AttacksFactory.create_attack(attack_name)
            if attack.is_compatible_with(pokemon.types):
                compatible_attacks.append(attack_name)
        except Exception as e:
            continue  # Si falla la creación, se omite
    
    # Seleccionar hasta num_attacks aleatorios de los compatibles (si hay menos, se asignan los disponibles)
    num_attacks = min(num_attacks, len(compatible_attacks))
    chosen_attacks = random.sample(compatible_attacks, num_attacks) if num_attacks > 0 else []
    
    # Asignar cada ataque al Pokémon
    for attack_name in chosen_attacks:
        attack = attacks.AttacksFactory.create_attack(attack_name)
        pokemon.learn_attack(attack)
    
    return pokemon

def create_random_pokemon(preferred_type=None):
    """
    Crea un Pokémon aleatorio basado en los datos disponibles en _species_data,
    asignándole 4 ataques compatibles.
    
    Parámetros:
      - preferred_type (str, opcional): el tipo preferido. Si se indica, habrá
        un 80% de probabilidad de que el Pokémon generado tenga ese tipo en sus atributos.
    
    Retorna:
      - Una instancia de Pokemon con 4 ataques asignados (si hay suficientes compatibles).
    """
    species_data = pokemons.PokemonFactory._species_data # Diccionario con especies disponibles
    all_species = list(species_data.keys())
    
    # Filtrar especies que contengan el tipo preferido en su lista de tipos
    species_preferred = []
    if preferred_type is not None:
        for specie in all_species:
            data = species_data[specie]
            # 'data' tiene un atributo 'types' (lista o tupla) con los tipos
            if preferred_type in data.get("types", []):
                species_preferred.append(specie)
    
    # Decidir la especie a generar
    prob = random.random()
    if preferred_type is not None and species_preferred and prob < 0.8:
        # 80% de probabilidad: elegir entre las especies que tengan el tipo preferido
        chosen_species = random.choice(species_preferred)
    elif preferred_type is not None and species_preferred and prob >= 0.8:
        # 20% de probabilidad: elegir de entre las que NO tengan el tipo preferido (si existen)
        species_not_preferred = [s for s in all_species if s not in species_preferred]
        chosen_species = random.choice(species_not_preferred) if species_not_preferred else random.choice(species_preferred)
    else:
        # Si no se pasa tipo preferido o no hay especies con ese tipo, se elige cualquier especie
        chosen_species = random.choice(all_species)
    
    # Crear el Pokémon usando la fábrica
    pokemon = pokemons.PokemonFactory.create_pokemon(chosen_species)
    # Asignar 4 ataques compatibles usando la función auxiliar
    assign_attacks_to_pokemon(pokemon, num_attacks=4)
    
    # Agregar el Pokémon a la lista global para que se "almacene"
    gs.pokemons.append(pokemon)
    return pokemon

def create_pokemon_by_species(species):
    """
    Crea un Pokémon de la especie especificada si la misma existe en los datos disponibles
    en _species_data, asignándole 4 ataques compatibles.
    
    Parámetros:
      - species (str, obligatorio): el nombre de la especie.
    
    Retorna:
      - Una instancia de Pokemon con 4 ataques asignados (si hay suficientes compatibles).
    """
    species_data = pokemons.PokemonFactory._species_data # Diccionario con especies disponibles

    if species not in species_data:
        raise ValueError(f"La especie '{species}' no existe en los datos disponibles.")
    
    # Crear el Pokémon usando la fábrica
    pokemon = pokemons.PokemonFactory.create_pokemon(species)
    # Asignar 4 ataques compatibles usando la función auxiliar
    assign_attacks_to_pokemon(pokemon, num_attacks=4)

    # Agregar el Pokémon a la lista global para que se "almacene"
    gs.pokemons.append(pokemon)
    return pokemon
