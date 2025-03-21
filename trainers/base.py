class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemons = []
        self.gym = None

    def add_pokemon(self, pokemon):
        # Validate that the Pokemon does not belongs to another trainer
        if pokemon.trainer is not None:
            raise ValueError(f"El Pokémon '{pokemon.name}' ya pertenece al entrenador {pokemon.trainer.name}.")
        pokemon.assign_trainer(self)
        self.pokemons.append(pokemon)

    def add_gym(self, gym):
        # Validate that the trainer does not belongs to another gym
        if self.gym is not None:
            raise ValueError(f"El entrenador '{self.name}' ya pertenece al gimnacio {self.gym.name}.")
        self.gym = gym

    def __repr__(self):
        return f"<Entrenador {self.name}: {self.pokemons}>"
