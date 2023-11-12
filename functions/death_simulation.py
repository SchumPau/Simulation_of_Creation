from classes.Creature import Creature
from classes.World import World
from classes.Food import Food
import random
import logging
import coloredlogs
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')

logger = logging.getLogger(__name__)
coloredlogs.install(level='INFO', logger=logger, fmt='[%(asctime)s] %(levelname)s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

def simulation_plot(food_items,creature,world):
    plt.scatter(creature.x, creature.y, s=100, c='red', marker='o')
    plt.scatter([f.x for f in food_items], [f.y for f in food_items], s=50, c='green', marker='o')
    plt.xlim(0, world.max_x)
    plt.ylim(0, world.max_y)
    plt.show()

def simulation():
    lim_x = 100
    lim_y = 100
    
    world = World(lim_x, lim_y)
    number_of_food = 100
    i = 0
    
    while len(world.food) < number_of_food:
        x_position = random.randint(0,lim_x)
        y_position = random.randint(0,lim_y)
        food_energy = random.randint(5,50)
        food = Food(x_position,y_position,food_energy)
            
        food_coordinates = [(f.x, f.y) for f in world.food]
        if (food.x, food.y) not in food_coordinates:
            world.food.append(food)
            logger.info(f"Food with X: {food.x} and Y: {food.y} and energy: {food.energy_provided} created!")
            i += 1
        
    creature = Creature(5, 5, 20, 1, world, "A")
    
    #simulation_plot(food_items,creature,world)
    
    gegessen = False
    
    while creature.energy > 0:
        creature.move()
        for food in world.food:           
            if creature.x == food.x and creature.y == food.y:
                creature.eat(food)
                world.food.remove(food)
                print("Food eaten")
                gegessen = True
                #break
        
        print(creature.x, creature.y, creature.energy)
    
    return gegessen