"""Example file for zoo project
It shows how zoos, cages and animals can be created, cages can be added to the zoo and animals can be
added to the cages
"""
from zoo_project import Cage, Animal, Zoo

zoo = Zoo("London Zoo")

cage1 = Cage()
cage2 = Cage()

zoo.add_cage(cage1)
zoo.add_cage(cage2)

print(zoo.count_cages())
print(zoo.cages)

freddie_the_lion = Animal("Freddie", "Lion")
bobby_the_sheep = Animal("Bobby", "Sheep")
turty_the_turtle = Animal("Turty", "Turtle")
flying_the_tiger = Animal("Flying", "Tiger")
linus_the_penguin = Animal("Linus", "Penguin")

cage1.add_animal(freddie_the_lion)
cage1.add_animal(bobby_the_sheep)
cage1.add_animal(turty_the_turtle)
cage2.add_animal(flying_the_tiger)
cage2.add_animal(linus_the_penguin)

print(cage1.animals)
print(cage2.animals)
