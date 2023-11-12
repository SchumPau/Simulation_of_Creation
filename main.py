from classes.Creature import Creature
from classes.World import World
from classes.Food import Food

number_of_food = 1000

food = Food(10,10,10,1)

world = World(10000, 10000)
creature = Creature(5, 5, 10, 1, world, "A")

while creature.energy > 0:
    creature.move()
    
    for i in range(number_of_food):
        if creature.x == food.x and creature.y == food.y:
            creature.eat(food)
            food = Food(10,10,0,1)
            print("Food eaten")
            break
    
    print(creature.x, creature.y, creature.energy)