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

    def add_animal(self, new_animal):
        """Adds an animal to the cage
        """
        # Checks if the animal has a list known of preys, if it does,
        # it's added to the cage and the existing animals
        # are checked against the list of preys, removing the ones that match
        # as they are eaten by the new predator.
        if hasattr(new_animal, 'preys'):
            for animal in self.animals:
                if animal.__class__ in new_animal.preys:
                    self.delete_animal(animal)
                    print(("{} just ate {}, this happened because you are placing predators \
                           in the same cages as their preys!")
                          .format(new_animal.name, animal.name))
            self.animals.append(new_animal)
        # If the new animal does not have known preys,
        # it may be that it is itself a prey, we check if any of the
        # existing animals is a predator for the new animal.
        # If this happen to be true,
        # the new animal will be eaten (deleted).
        else:
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


class Lion(Animal):

    """Species class will define the specific characteristics
    of the animals that are not shared between them
    """

    def __init__(self, name):
        super().__init__(name)
        self.species = "Lion"
        # If the animal species has known preys,
        # they will be added as the prey property of the animal,
        #  to be used when the animal is added to the cage.
        self.preys = [Sheep, Wildebeest, Impala, Zebra,
                      Giraffe, Buffalo, WildHog, Rhinoceros,
                      Hippopotamus]

    def __str__(self):
        return "{} the {}".format(self.name, self.species)


class Tiger(Animal):

    """Species class will define the specific characteristics
    of the animals that are not shared between them
    """

    def __init__(self, name):
        super().__init__(name)
        self.species = "Lion"
        # If the animal species has known preys,
        # they will be added as the prey property of the animal,
        #  to be used when the animal is added to the cage.
        self.preys = [Impala, Gazelles, Wildebeest,
                      Zebra, Goat, Sheep, Horse]

    def __str__(self):
        return "{} the {}".format(self.name, self.species)


class Hyena(Animal):

    """Species class will define the specific characteristics
    of the animals that are not shared between them
    """

    def __init__(self, name):
        super().__init__(name)
        self.species = "Lion"
        # If the animal species has known preys,
        # they will be added as the prey property of the animal,
        #  to be used when the animal is added to the cage.
        self.preys = [Boar, WildPig, Bear, Buffalo,
                      WildCattle, Deer, Antelopes, Monkey]

    def __str__(self):
        return "{} the {}".format(self.name, self.species)


class Turtle(Animal):

    """Species class will define the specific
    characteristics of the animals that are not shared between them
    """

    def __init__(self, name):
        super().__init__(name)
        self.species = "Turtle"

    def __str__(self):
        return "{} the {}".format(self.name, self.species)


class Antelopes(Animal):

    """Species class will define the specific
    characteristics of the animals that are not shared between them
    """

    def __init__(self, name):
        super().__init__(name)
        self.species = "Antelopes"

    def __str__(self):
        return "{} the {}".format(self.name, self.species)


class Monkey(Animal):

    """Species class will define the specific
    characteristics of the animals that are not shared between them
    """

    def __init__(self, name):
        super().__init__(name)
        self.species = "Monkey"

    def __str__(self):
        return "{} the {}".format(self.name, self.species)


class Wildebeest(Animal):

    """Species class will define the specific
    characteristics of the animals that are not shared between them
    """

    def __init__(self, name):
        super().__init__(name)
        self.species = "Wildebeest"

    def __str__(self):
        return "{} the {}".format(self.name, self.species)


class Boar(Animal):

    """Species class will define the specific
    characteristics of the animals that are not shared between them
    """

    def __init__(self, name):
        super().__init__(name)
        self.species = "Boar"

    def __str__(self):
        return "{} the {}".format(self.name, self.species)


class WildPig(Animal):

    """Species class will define the specific
    characteristics of the animals that are not shared between them
    """

    def __init__(self, name):
        super().__init__(name)
        self.species = "WildPig"

    def __str__(self):
        return "{} the {}".format(self.name, self.species)


class Bear(Animal):

    """Species class will define the specific
    characteristics of the animals that are not shared between them
    """

    def __init__(self, name):
        super().__init__(name)
        self.species = "Bear"

    def __str__(self):
        return "{} the {}".format(self.name, self.species)


class WildCattle(Animal):

    """Species class will define the specific
    characteristics of the animals that are not shared between them
    """

    def __init__(self, name):
        super().__init__(name)
        self.species = "WildCattle"

    def __str__(self):
        return "{} the {}".format(self.name, self.species)


class Deer(Animal):

    """Species class will define the specific
    characteristics of the animals that are not shared between them
    """

    def __init__(self, name):
        super().__init__(name)
        self.species = "Deer"

    def __str__(self):
        return "{} the {}".format(self.name, self.species)


class Impala(Animal):

    """Species class will define the specific
    characteristics of the animals that are not shared between them
    """

    def __init__(self, name):
        super().__init__(name)
        self.species = "Impala"

    def __str__(self):
        return "{} the {}".format(self.name, self.species)


class Zebra(Animal):

    """Species class will define the specific
    characteristics of the animals that are not shared between them
    """

    def __init__(self, name):
        super().__init__(name)
        self.species = "Zebra"

    def __str__(self):
        return "{} the {}".format(self.name, self.species)


class Giraffe(Animal):

    """Species class will define the specific
    characteristics of the animals that are not shared between them
    """

    def __init__(self, name):
        super().__init__(name)
        self.species = "Giraffe"

    def __str__(self):
        return "{} the {}".format(self.name, self.species)


class Buffalo(Animal):

    """Species class will define the specific
    characteristics of the animals that are not shared between them
    """

    def __init__(self, name):
        super().__init__(name)
        self.species = "Buffalo"

    def __str__(self):
        return "{} the {}".format(self.name, self.species)


class WildHog(Animal):

    """Species class will define the specific
    characteristics of the animals that are not shared between them
    """

    def __init__(self, name):
        super().__init__(name)
        self.species = "WildHog"

    def __str__(self):
        return "{} the {}".format(self.name, self.species)


class Rhinoceros(Animal):

    """Species class will define the specific
    characteristics of the animals that are not shared between them
    """

    def __init__(self, name):
        super().__init__(name)
        self.species = "Rhinoceros"

    def __str__(self):
        return "{} the {}".format(self.name, self.species)


class Hippopotamus(Animal):

    """Species class will define the specific
    characteristics of the animals that are not shared between them
    """

    def __init__(self, name):
        super().__init__(name)
        self.species = "Hippopotamus"

    def __str__(self):
        return "{} the {}".format(self.name, self.species)


class Gazelles(Animal):

    """Species class will define the specific
    characteristics of the animals that are not shared between them
    """

    def __init__(self, name):
        super().__init__(name)
        self.species = "Gazelles"

    def __str__(self):
        return "{} the {}".format(self.name, self.species)


class Goat(Animal):

    """Species class will define the specific
    characteristics of the animals that are not shared between them
    """

    def __init__(self, name):
        super().__init__(name)
        self.species = "Goat"

    def __str__(self):
        return "{} the {}".format(self.name, self.species)


class Horse(Animal):

    """Species class will define the specific
    characteristics of the animals that are not shared between them
    """

    def __init__(self, name):
        super().__init__(name)
        self.species = "Horse"

    def __str__(self):
        return "{} the {}".format(self.name, self.species)


class Sheep(Animal):

    """Species class will define the specific
    characteristics of the animals that are not shared between them
    """

    def __init__(self, name):
        super().__init__(name)
        self.species = "Sheep"

    def __str__(self):
        return "{} the {}".format(self.name, self.species)
