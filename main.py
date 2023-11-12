from classes.Creature import Creature
from classes.World import World

world = World(10, 10)
creature = Creature(5, 5, 10, 1, world, "A")

while creature.energy > 0:
    creature.move()
    print(creature.x, creature.y, creature.energy)