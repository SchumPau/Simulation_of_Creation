from classes.Creature import Creature
from classes.World import World
from classes.Food import Food
from functions.creation_creatures import create_creature
import random
import logging
import coloredlogs
from typing import List

logger = logging.getLogger(__name__)
coloredlogs.install(level='INFO', logger=logger, fmt='[%(asctime)s] %(levelname)s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')


def simulation(number_of_food: int, number_of_creature: int, first_round: bool, creatures: List[Creature], world: World, existing_food: int):
    
    # Implementation variables
    death_creatures = []
    i = 0
    #creatures = []
    dead = False
    lim_x = world.max_x
    lim_y = world.max_y
    
    number_of_food = number_of_food + existing_food
    
    # Create world
    # world = World(lim_x, lim_y)
    
    # Creating Food    
    while len(world.food) < number_of_food:
        x_position = random.randint(0,lim_x)
        y_position = random.randint(0,lim_y)
        food_energy = random.randint(5,15)
        food = Food(x_position,y_position,food_energy)
        
        # Listing of all Food and send it to world
        food_coordinates = [(f.x, f.y) for f in world.food]
        
        # Check for existing Food
        if (food.x, food.y) not in food_coordinates:
            world.food.append(food)
            logger.info(f"Food with X: {food.x} and Y: {food.y} and energy: {food.energy_provided} created!")
            i += 1
    
    # Simulation
    while len(creatures) > 0:
        logger.debug(f"Number of Creatures: {len(creatures)}")
        
        # Shuffle of Creatures
        random.shuffle(creatures)
        logger.debug(f"Creatures shuffled")
        
        for creature in creatures:
            logger.debug(f"Simulate Creature: {creature}")
            if creature.energy > 0:
                creature.move()
                
                # Check for Food
                for food in world.food:           
                    if creature.x == food.x and creature.y == food.y:
                        creature.eat(food)
                        world.food.remove(food)
                        logger.info("Food eaten")
                        #break
                    
                # Debug actual position and energy
                logger.debug(f"Position of Creature: {creature.x}, {creature.y}, Energy: {creature.energy}")
            else:
                # Creature died because of energy
                death_creatures.append(creature)
                creature.death()
                creatures.remove(creature)                    
                logger.info("Creature died")
    
    # return last 4 creatures
    logger.info(f"Round finished, best 4 creatures: {death_creatures[-4:]}")
    return death_creatures[-4:], world.food