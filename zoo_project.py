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

    def __str__(self):
        return "This is {} Zoo, it has {} cages".format(self.name,
                                                        self.count_cages())


class Cage:

    """Definition of the zoo cages.
    It needs a zoo for the cage
    """
    cage_counter = 1

    def add_predator(self, new_animal):
        """Adds a predator to the cage
            When a predator it's added to the cage the existing animals
            are checked against the list of preys, removing the ones that match
            as they are eaten by the new predator.
        """
        for animal in self.animals:
            if animal.__class__ in new_animal.preys:
                self.delete_animal(animal)
                print(("{} just ate {}, this happened because you are placing predators \
                       in the same cages as their preys!")
                      .format(new_animal.name, animal.name))
        self.animals.append(new_animal)

    def add_prey(self, new_animal):
        """Adds a prey, which is animal with no preys, to the cage
            it may be that it is itself a prey, we check if any of the
            existing animals is a predator for the new animal.
            If this happen to be true,
            the new animal will be eaten (deleted).
        """
        for animal in self.animals:
            if hasattr(animal, 'preys'):
                if new_animal.__class__ in animal.preys:
                    print(("{} has just been eaten by {},\
                        this happened because you are placing predators \
                        in the same cages as their preys!").format(
                        new_animal.name,
                        animal.name))
                    del(new_animal)
                    return
        self.animals.append(new_animal)

    def add_animal(self, new_animal):
        """Adds an animal to the cage
        """
        # Checks if the animal has a list known of preys, if it does
        # it calls the add_predator property
        if hasattr(new_animal, 'preys'):
            Cage.add_predator(self, new_animal)
        # If the new animal does not have known preys,
        # it calls the add_prey property
        else:
            Cage.add_prey(self, new_animal)

    def delete_animal(self, animal):
        """ Deletes animals from the cage,
        this can be a manual action by the zoo
        keeper or due to a predator eating preys
        """
        self.animals.remove(animal)

    def __init__(self):
        self.animals = []
        self.cage_number = Cage.cage_counter
        Cage.cage_counter += 1

    def __str__(self):
        return "This is the cage number {}\
        and it contains the following animals {}".format(self.cage_number,
                                                         self.animals)


class Animal:

    """Creates an animal
    name
    """

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "{}".format(self.name)

# Defining preys first as they will be used by the predators


class Turtle(Animal):

    """Species class will define the specific
    characteristics of the animals that are not shared between them
    """
    species = "Turtle"

    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return "{} the {}".format(self.name, self.species)


class Antelopes(Animal):

    """Species class will define the specific
    characteristics of the animals that are not shared between them
    """
    species = "Antelopes"

    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return "{} the {}".format(self.name, self.species)


class Monkey(Animal):

    """Species class will define the specific
    characteristics of the animals that are not shared between them
    """
    species = "Monkey"

    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return "{} the {}".format(self.name, self.species)


class Wildebeest(Animal):

    """Species class will define the specific
    characteristics of the animals that are not shared between them
    """
    species = "Wildebeest"

    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return "{} the {}".format(self.name, self.species)


class Boar(Animal):

    """Species class will define the specific
    characteristics of the animals that are not shared between them
    """
    species = "Boar"

    def __init__(self, name):
        super().__init__(name)
        self.species = "Boar"

    def __str__(self):
        return "{} the {}".format(self.name, self.species)


class WildPig(Animal):

    """Species class will define the specific
    characteristics of the animals that are not shared between them
    """
    species = "WildPig"

    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return "{} the {}".format(self.name, self.species)


class Bear(Animal):

    """Species class will define the specific
    characteristics of the animals that are not shared between them
    """
    species = "Bear"

    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return "{} the {}".format(self.name, self.species)


class WildCattle(Animal):

    """Species class will define the specific
    characteristics of the animals that are not shared between them
    """
    species = "WildCattle"

    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return "{} the {}".format(self.name, self.species)


class Deer(Animal):

    """Species class will define the specific
    characteristics of the animals that are not shared between them
    """
    species = "Deer"

    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return "{} the {}".format(self.name, self.species)


class Impala(Animal):

    """Species class will define the specific
    characteristics of the animals that are not shared between them
    """
    species = "Impala"

    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return "{} the {}".format(self.name, self.species)


class Zebra(Animal):

    """Species class will define the specific
    characteristics of the animals that are not shared between them
    """
    species = "Zebra"

    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return "{} the {}".format(self.name, self.species)


class Giraffe(Animal):

    """Species class will define the specific
    characteristics of the animals that are not shared between them
    """
    species = "Giraffe"

    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return "{} the {}".format(self.name, self.species)


class Buffalo(Animal):

    """Species class will define the specific
    characteristics of the animals that are not shared between them
    """
    species = "Buffalo"

    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return "{} the {}".format(self.name, self.species)


class WildHog(Animal):

    """Species class will define the specific
    characteristics of the animals that are not shared between them
    """
    species = "WildHog"

    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return "{} the {}".format(self.name, self.species)


class Rhinoceros(Animal):

    """Species class will define the specific
    characteristics of the animals that are not shared between them
    """
    species = "Rhinoceros"

    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return "{} the {}".format(self.name, self.species)


class Hippopotamus(Animal):

    """Species class will define the specific
    characteristics of the animals that are not shared between them
    """
    species = "Hippopotamus"

    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return "{} the {}".format(self.name, self.species)


class Gazelles(Animal):

    """Species class will define the specific
    characteristics of the animals that are not shared between them
    """
    species = "Gazelles"

    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return "{} the {}".format(self.name, self.species)


class Goat(Animal):

    """Species class will define the specific
    characteristics of the animals that are not shared between them
    """
    species = "Goat"

    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return "{} the {}".format(self.name, self.species)


class Horse(Animal):

    """Species class will define the specific
    characteristics of the animals that are not shared between them
    """
    species = "Horse"

    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return "{} the {}".format(self.name, self.species)


class Sheep(Animal):

    """Species class will define the specific
    characteristics of the animals that are not shared between them
    """
    species = "Sheep"

    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return "{} the {}".format(self.name, self.species)


# Predators definitions


class Lion(Animal):

    """Species class will define the specific characteristics
    of the animals that are not shared between them
    """
    # If the animal species has known preys,
    # they will be added as the prey property of the animal,
    #  to be used when the animal is added to the cage.
    species = "Lion"
    preys = [Sheep, Wildebeest, Impala, Zebra,
             Giraffe, Buffalo, WildHog, Rhinoceros,
             Hippopotamus]

    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return "{} the {}".format(self.name, self.species)


class Tiger(Animal):

    """Species class will define the specific characteristics
    of the animals that are not shared between them
    """
    # If the animal species has known preys,
    # they will be added as the prey property of the animal,
    #  to be used when the animal is added to the cage.
    species = "Tiger"
    preys = [Impala, Gazelles, Wildebeest,
             Zebra, Goat, Sheep, Horse]

    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return "{} the {}".format(self.name, self.species)


class Hyena(Animal):

    """Species class will define the specific characteristics
    of the animals that are not shared between them
    """

    # If the animal species has known preys,
    # they will be added as the prey property of the animal,
    #  to be used when the animal is added to the cage.
    species = "Hyena"
    preys = [Boar, WildPig, Bear, Buffalo,
             WildCattle, Deer, Antelopes, Monkey]

    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return "{} the {}".format(self.name, self.species)
