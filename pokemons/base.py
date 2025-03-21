import uuid
import pokemons

class Pokemon:
    #_registro = {} # Avoids duplicates globaly
    MAX_TYPES = 2 # Max number of types allowed

    def __init__(self, name, types, damage, level, base_hp):
        # Validate that types is a list or tuple and that doesn't exceeds the maximum allowed
        if not isinstance(types, (list, tuple)):
            raise ValueError("El atributo 'types' debe ser una lista o tupla.")
        if len(types) > Pokemon.MAX_TYPES:
            raise ValueError(f"Un Pokémon no puede tener más de {Pokemon.MAX_TIPOS} tipos.")
        
        # Unique identifier (string) for the Pokémon
        self.id = str(uuid.uuid4())

        self.name = name
        self.types = list(types)
        self.damage = damage
        self.level = level
        self.base_hp = base_hp
        self.trainer = None # Initially , has no trainer
        self.attacks = []   # List of attacks that can learn
        self.hp = self.base_hp + self.level * 3
        self.max_hp = self.hp

    def assign_trainer(self, trainer):
        if self.trainer is not None:
            raise ValueError(f"El Pokémon '{self.name}' (ID: {self.id}) ya pertenece al entrenador {self.trainer.name}.")
        self.trainer = trainer

    def learn_attack(self, attack):
        # Allows learning the attack if at least one of the types os compatible
        if not attack.is_compatible_with(self.types):
            raise ValueError(
                f"El ataque '{attack.name}' no es compatible con los tipos {self.types} de este Pokémon."
            )
        self.attacks.append(attack)

    def __repr__(self):
        return f"<Pokemon {self.name} (ID: {self.id}, Tipos: {self.types})>"
    
class PokemonFactory:
    _species_data = {
        "Pikachu": pokemons.electric.pikachu,
        "Squirtle": pokemons.water.squirtle,
        "Lairon": pokemons.steel.lairon,
        "Zapdos": pokemons.electric.zapdos,
        "Hitmonchan": pokemons.fighting.hitmonchan,
    }

    @staticmethod
    def create_pokemon(name):
        if name not in PokemonFactory._species_data:
            raise ValueError(f"No hay datos para la especie '{name}'.")
        
        data = PokemonFactory._species_data[name]
        return Pokemon(name=name, **data)