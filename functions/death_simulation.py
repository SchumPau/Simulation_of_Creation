from classes.Creature import Creature
from classes.World import World
from classes.Food import Food
from functions.functions import *

def simulation():
    lim_x = 10000
    lim_y = 10000
    
    world = World(lim_x, lim_y)
    number_of_food = 10000
    food_items = []
    
    for i in range(number_of_food):
        x_position = random.randint(lim_x)
        y_position = random.randint(lim_y)
        food_energy = random.randint(5,50)
        food = Food(x_position,y_position,food_energy,1)
        food_items.append(food)
        
    food = Food(10,10,10,1)
        
    creature = Creature(5, 5, 10, 1, world, "A")
    
    while creature.energy > 0:
        creature.move()
        
        if creature.x == food.x and creature.y == food.y:
            creature.eat(food)
            food = Food(10,10,0,1)
            print("Food eaten")
            break
        
        print(creature.x, creature.y, creature.energy)