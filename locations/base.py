from abc import ABC, abstractmethod
import data.game_state as gs

class Location(ABC):
    def __init__(self, name, icon, x, y):
        self.name = name
        self.icon = icon
        self.x = x  # Coordenada horizontal
        self.y = y  # Coordenada vertical

    @abstractmethod
    def validate(self):
        """Método abstracto para validar la unicidad de la ubicación."""
        pass

    def __repr__(self):
        return f"<Locaci'on {self.name} en ({self.x}, {self.y})>"

class Gym(Location):
    def __init__(self, name, icon, x, y, type_):
        super().__init__(name, icon, x, y)
        self.type_ = type_
        self.trainers = []  # Lista de entrenadores

        self.validate()  # Valida la nueva instancia

        # Una vez validada, se agrega a las listas globales
        gs.gyms.append(self)
        gs.locations.append(self)

    def validate(self):
        # Recorremos los gimnasios existentes para asegurar que
        # el icono, la x y la y sean únicos.
        for gym in gs.gyms:
            if gym.icon == self.icon or (gym.x == self.x and gym.y == self.y):
                raise ValueError("El gimnasio debe tener un icono único y coordenadas únicas.")

    def add_trainer(self, trainer):
        if trainer in self.trainers:
            raise ValueError(f"El entrenador {trainer.name} ya está asignado a este gimnasio.")
        self.trainers.append(trainer)
        trainer.add_gym(self)  # Asigna el gimnasio al entrenador

    def __repr__(self):
        return f"<Gimnacio {self.name} ({self.type_}) en ({self.x}, {self.y}) - Entrenadores: {len(self.trainers)}>"

class Hospital(Location):
    _id_counter = 1  # Atributo de clase para llevar la cuenta

    def __init__(self, name, icon, x, y):
        super().__init__(name, icon, x, y)
        self.id = Hospital._id_counter
        Hospital._id_counter += 1

        self.validate()  # Valida la nueva instancia

        # Se agrega a las listas globales correspondientes
        gs.hospitals.append(self)
        gs.locations.append(self)

    def validate(self):
        # Solo se validan las coordenadas (x, y)
        for hospital in gs.hospitals:
            if hospital.x == self.x and hospital.y == self.y:
                raise ValueError("El hospital debe tener coordenadas únicas.")

    def __repr__(self):
        return f"<Hospital {self.name} en ({self.x}, {self.y})>"
