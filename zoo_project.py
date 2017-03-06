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
        return "This is {} Zoo, it has {} cages".format(self.name, self.count_cages())


class Cage:
    """Definition of the zoo cages.
    It needs a zoo for the cage
    """
    cage_counter = 1

    def add_animal(self, new_animal):
        """Adds an animal to the cage
        """
        # Checks if the animal has a list known of preys, if it does, it's added to the cage and the existing animals
        #  are checked against the list of preys, removing the ones that match as they are eaten by the new predator.
        if hasattr(new_animal, 'preys'):
            for animal in self.animals:
                if animal.animal_species.lower() in new_animal.preys:
                    self.delete_animal(animal)
                    print(("{} just ate {}, this happened because you are placing predators"
                           "in the same cages as their preys!")
                          .format(new_animal.animal_name, animal.animal_name))
            self.animals.append(new_animal)
        # If the new animal does not have known preys, it may be that it is itself a prey, we check if any of the
        # existing animals is a predator for the new animal. If this happen to be true,
        # the new animal will be eaten (deleted).
        else:
            for animal in self.animals:
                if hasattr(animal, 'preys'):
                    if new_animal.animal_species.lower() in animal.preys:
                        print(("{} has just been eaten by {}, this happened because you are placing predators"
                               "in the same cages as their preys!").format(new_animal.animal_name, animal.animal_name))
                        del(new_animal)
                        return
            self.animals.append(new_animal)

    def delete_animal(self, animal):
        """ Deletes animals from the cage, this can be a manual action by the zoo keeper or due to a predator eating preys
        """
        self.animals.remove(animal)

    def __init__(self):
        self.animals = []
        self.cage_number = Cage.cage_counter
        Cage.cage_counter += 1

    def __repr__(self):
        return "This is the cage number {} and it contains the following animals {}".format(self.cage_number,
                                                                                            self.animals)


class Animal:
    """Adds an animal to a cage, required attributes are:
    animal_species
    animal_name
    cage
    """

    def __init__(self, animal_name, animal_species):
        self.animal_name = animal_name
        self.animal_species = animal_species
        # If the animal species has known preys, they will be added as the prey property of the animal,
        #  to be used when the animal is added to the cage.
        if animal_species.lower() == "lion":
            self.preys = ["sheep", "wildebeest", "impala", "zebra", "giraffe", "buffalo", "wild hog", "rhinoceros",
                          "hippopotamus"]
        if animal_species.lower() == "tiger":
            self.preys = ["boar", "wild pig", "bear", "buffalo", "wild cattle", "deer", "antelopes", "monkey"]
        if animal_species.lower() == "hyena":
            self.preys = ["impalas", "gazelles", "wildebeests", "zebras", "goat", "sheep", "horse"]

    def __repr__(self):
        return "{} the {}".format(self.animal_name, self.animal_species)
