class Gym:
    def __init__(self, name, type_, icon):
        self.name = name
        self.type = type_
        self.icon = icon
        self.trainers = []  # List of trainers

    def add_trainer(self, trainer):
        if trainer in self.trainers:
            raise ValueError(f"El entrenador {trainer.name} ya está asignado a este gimnasio.")
        self.trainers.append(trainer)
        trainer.add_gym(self)  # assign de gym to the trainer

    def __repr__(self):
        return f"<Gym {self.name} ({self.type}) - Entrenadores: {len(self.trainers)}>"
