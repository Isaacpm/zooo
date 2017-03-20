import unittest

from zoo_project import Zoo, Cage, Animal, Tiger, Sheep, Turtle, Hyena, Lion


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


class TestLionCreation(unittest.TestCase):
    """Creates an animal and checks that the name corresponds to the one we used at creation time.
    """

    def test_animal(self):
        freddie = Lion("Freddie")
        self.assertEqual(freddie.name, 'Freddie')


class TestTigerCreation(unittest.TestCase):
    """Creates an animal and checks that the name corresponds to the one we used at creation time.
    """

    def test_animal(self):
        tigress = Tiger("Tigress")
        self.assertEqual(tigress.name, 'Tigress')


class TestHyenaCreation(unittest.TestCase):
    """Creates an animal and checks that the name corresponds to the one we used at creation time.
    """

    def test_animal(self):
        banzay = Hyena("Banzay")
        self.assertEqual(banzay.name, 'Banzay')


class TestTurtleCreation(unittest.TestCase):
    """Creates an animal and checks that the name corresponds to the one we used at creation time.
    """

    def test_animal(self):
        leonardo = Turtle("Leonardo")
        self.assertEqual(leonardo.name, 'Leonardo')


class TestSheepCreation(unittest.TestCase):
    """Creates an animal and checks that the name corresponds to the one we used at creation time.
    """

    def test_animal(self):
        dolly = Sheep("Dolly")
        self.assertEqual(dolly.name, 'Dolly')


class TestAddAnimalToCage(unittest.TestCase):
    """Creates an animal, adds it to the cage and checks that the cage contains an animal with the right name in the text.
    """

    def test_add_animal_to_cage(self):
        freddie = Lion("Freddie")
        cage = Cage()
        cage.add_animal(freddie)
        self.assertEqual(cage.animals, [freddie])


class TestDeleteAnimalFromCage(unittest.TestCase):
    """Creates and adds two animals to a cage, then deletes one and expects the number of animals in the cage to be 1.
    """

    def test_delete_animal_from_cage(self):
        freddie = Lion("Freddie")
        leonardo = Turtle("Leonardo")
        cage = Cage()
        cage.add_animal(freddie)
        cage.add_animal(leonardo)
        cage.delete_animal(freddie)
        self.assertEqual(cage.animals, [leonardo])


class TestPredatorEatsPrey(unittest.TestCase):
    """Creates and adds two animals to a cage, one of them it's a predator and the other one is a prey.
    Expects the number of animals in the cage to be 1.
    This is tested in two different ways, first adding a predator and then a prey. And secondly adding the prey first.
    Both behaviours should result in the predator being left on its own.
    """

    def test_predator_eats_new_prey(self):
        freddie = Lion("Freddie")
        dolly = Sheep("Dolly")
        cage = Cage()
        cage.add_animal(freddie)
        cage.add_animal(dolly)
        self.assertEqual(cage.animals, [freddie])

    def test_new_predator_eats_prey(self):
        dolly = Sheep("Dolly")
        freddie = Lion("Freddie")
        cage = Cage()
        cage.add_animal(dolly)
        cage.add_animal(freddie)
        self.assertEqual(cage.animals, [freddie])


class TestPredatorDoesntEatAnimalNotInList(unittest.TestCase):
    """Creates a predator and a prey, in this case the prey is not in the predator's prey list, so it survives.
    """

    def test_predator_eats_new_prey(self):
        freddie = Lion("Freddie")
        leonardo = Turtle("Leonardo")
        cage = Cage()
        cage.add_animal(freddie)
        cage.add_animal(leonardo)
        self.assertEqual(cage.animals, [freddie, leonardo])


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
