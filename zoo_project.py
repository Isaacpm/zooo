"""Creates a series of different cages for the Zoo
"""


class Zoo:
    """Defines a Zoo and stores the cages in it
    """

    def add_cage(self, cage):
        """Adds a cage to the current list of cages
        """
        self.cages.append(cage)

    def count_cages(self):
        """Counts the number of cages
        """
        number_of_cages = len(self.cages)

        return number_of_cages

    def __init__(self, name):
        self.cages = []
        self.name = name

    def __repr__(self):
        return self.name


class Cage:
    """Definition of the zoo cages.
    It needs a zoo for the cage
    """
    cage_counter = 1

    def add_animal(self, animal):
        """Adds an animal to the cage
        """
        if len(self.animals):
            if animal.predator != self.animals[0].predator:
                raise Exception("You are mixing predators with preys!")
        self.animals.append(animal)

    def __init__(self):
        self.animals = []
        self.cage_number = Cage.cage_counter
        Cage.cage_counter += 1

    def __repr__(self):
        return str(self.cage_number)



class Animal:
    """Adds an animal to a cage, required attributes are:
    animal_species
    animal_name
    cage
    predator
    """

    def __init__(self, animal_name, animal_species, predator):
        self.animal_name = animal_name
        self.animal_species = animal_species
        self.predator = predator

    def __repr__(self):
        return self.animal_name