"""
Single Responsibility Principle
A class should have only one job.  If a class has more than one responsibility
it becomes coupled.  A change to one responsibility results to modification of
the other responsibility.
"""


class Animal:
    def __init__(self, name: str):
        self.name = name

    def get_name(self) -> str:
        pass

    def save(self, animal: Animal):
        pass


"""
The Animal class violates the SRP.

SRP states that classes should have one responsibility, here, we can draw out
two responsibilities: animal database management and animal properties
management.  The constructor and get_name manage the Animal properties while the
save manages the Animal storage on a database.

To make this conform to SRP, we create another class that will handle the sole
responsibility of storing an animal to a database:
"""


class Animal:
    def __init__(self, name: str):
        self.name = name

    def get_name(self) -> str:
        pass


class AnimalDB:
    def get_animal(self, id) -> Animal:
        pass

    def save(self, animal: Animal):
        pass
