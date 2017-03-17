import unittest
from zoo_project import Cage, Animal, Zoo


class TestZooCreation(unittest.TestCase):
    """Just creates a Zoo and checks the name is the same one we used at creation time.
    """

    def test_zoo(self):
        zoo = Zoo("London Zoo")
        self.assertEqual(zoo.name, 'London Zoo')


class TestCageCreation(unittest.TestCase):
    """Creates a cage
    """

    def test_cage(self):
        cage = Cage()


class TestAnimalCreation(unittest.TestCase):
    """Creates an animal and checks that the name corresponds to the one we used at creation time.
    """

    def test_animal(self):
        freddie_the_lion = Animal("Freddie", "Lion")
        self.assertEqual(freddie_the_lion.name, 'Freddie')


class TestAddAnimalToCage(unittest.TestCase):
    """Creates an animal, adds it to the cage and checks that the cage contains an animal with the right name in the text.
    """

    def test_add_animal_to_cage(self):
        freddie_the_lion = Animal("Freddie", "Lion")
        cage = Cage()
        cage.add_animal(freddie_the_lion)
        self.assertEqual(cage.animals, [freddie_the_lion])


class TestDeleteAnimalFromCage(unittest.TestCase):
    """Creates and adds two animals to a cage, then deletes one and expects the number of animals in the cage to be 1.
    """

    def test_delete_animal_from_cage(self):
        freddie_the_lion = Animal("Freddie", "Lion")
        turty_the_turtle = Animal("Turty", "Turtle")
        cage = Cage()
        cage.add_animal(freddie_the_lion)
        cage.add_animal(turty_the_turtle)
        cage.delete_animal(freddie_the_lion)
        self.assertEqual(cage.animals, [turty_the_turtle])


class TestPredatorEatsPrey(unittest.TestCase):
    """Creates and adds two animals to a cage, one of them it's a predator and the other one is a prey.
    Expects the number of animals in the cage to be 1.
    This is tested in two different ways, first adding a predator and then a prey. And secondly adding the prey first.
    Both behaviours should result in the predator being left on its own.
    """

    def test_predator_eats_new_prey(self):
        freddie_the_lion = Animal("Freddie", "Lion")
        bobby_the_sheep = Animal("Bobby", "Sheep")
        cage = Cage()
        cage.add_animal(freddie_the_lion)
        cage.add_animal(bobby_the_sheep)
        self.assertEqual(cage.animals, [freddie_the_lion])

    def test_new_predator_eats_prey(self):
        freddie_the_lion = Animal("Freddie", "Lion")
        bobby_the_sheep = Animal("Bobby", "Sheep")
        cage = Cage()
        cage.add_animal(bobby_the_sheep)
        cage.add_animal(freddie_the_lion)
        self.assertEqual(cage.animals, [freddie_the_lion])


class TestPredatorDoesntEatAnimalNotInList(unittest.TestCase):
    """Creates a predator and a prey, in this case the prey is not in the predator's prey list, so it survives.
    """

    def test_predator_eats_new_prey(self):
        freddie_the_lion = Animal("Freddie", "Lion")
        turty_the_turtle = Animal("Turty", "Turtle")
        cage = Cage()
        cage.add_animal(freddie_the_lion)
        cage.add_animal(turty_the_turtle)
        self.assertEqual(cage.animals, [freddie_the_lion,turty_the_turtle])


class TestAddCageToZoo(unittest.TestCase):
    """Creates an animal, adds it to the cage and checks that the cage contains an animal with the right name in the text.
    """

    def test_upper(self):
        zoo = Zoo("London Zoo")
        cage = Cage()
        zoo.add_cage(cage)
        self.assertEqual(zoo.count_cages(), 1)


if __name__ == '__main__':
    unittest.main()
