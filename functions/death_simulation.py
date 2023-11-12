from classes.Creature import Creature
from classes.World import World
from classes.Food import Food
import random
import logging
import coloredlogs

logger = logging.getLogger(__name__)
coloredlogs.install(level='INFO', logger=logger, fmt='[%(asctime)s] %(levelname)s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

def simulation_plot(food_items, creature, world):
    import matplotlib.pyplot as plt
    import numpy as np
    import matplotlib.animation as animation
    from matplotlib import style
    style.use('fivethirtyeight')
    
    fig = plt.figure()
    ax1 = fig.add_subplot(1,1,1)
    
    def animate(i):
        x = []
        y = []
        for food in food_items:
            x.append(food.x)
            y.append(food.y)
        x.append(creature.x)
        y.append(creature.y)
        ax1.clear()
        ax1.scatter(x,y)
        ax1.set_xlim(0,world.max_x)
        ax1.set_ylim(0,world.max_y)
    
    ani = animation.FuncAnimation(fig, animate, interval=100)
    plt.show()

def simulation():
    lim_x = 100
    lim_y = 100
    
    world = World(lim_x, lim_y)
    number_of_food = 100
    food_items = []
    i = 0
    
    while i < number_of_food:
        x_position = random.randint(0,lim_x)
        y_position = random.randint(0,lim_y)
        food_energy = random.randint(5,50)
        food = Food(x_position,y_position,food_energy,1)
            
        food_coordinates = [(f.x, f.y) for f in food_items]
        if (food.x, food.y) not in food_coordinates:
            food_items.append(food)
            logger.info(f"Food with X: {food.x} and Y: {food.y} and energy: {food.energy_provided} created!")
            i += 1
        
    creature = Creature(5, 5, 10, 1, world, "A")
    
    simulation_plot(food_items,creature,world)
    
    while creature.energy > 0:
        creature.move()
        for food in food_items:           
            if creature.x == food.x and creature.y == food.y:
                creature.eat(food)
                food.energy_provided = 0
                print("Food eaten")
                break
        
        print(creature.x, creature.y, creature.energy)