from classes.Creature import Creature
from classes.World import World
from classes.Food import Food
from functions.Creation_Creatures import Create_Creature
import random
import logging
import coloredlogs

logger = logging.getLogger(__name__)
coloredlogs.install(level='DEBUG', logger=logger, fmt='[%(asctime)s] %(levelname)s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')


def simulation(lim_x,lim_y,number_of_food,number_of_creature,first_round,creatures,world):
    
    # Implementation variables
    next_generation = []
    i = 0
    #creatures = []
    dead = False
    
    # Create world
    # world = World(lim_x, lim_y)
    
    # Creating Food    
    while len(world.food) < number_of_food:
        x_position = random.randint(0,lim_x)
        y_position = random.randint(0,lim_y)
        food_energy = random.randint(5,25)
        food = Food(x_position,y_position,food_energy)
        
        # Listing of all Food and send it to world
        food_coordinates = [(f.x, f.y) for f in world.food]
        
        # Check for existing Food
        if (food.x, food.y) not in food_coordinates:
            world.food.append(food)
            logger.info(f"Food with X: {food.x} and Y: {food.y} and energy: {food.energy_provided} created!")
            i += 1
    
    if first_round == True:
        creatures = Create_Creature(number_of_creature,lim_x,lim_y,world)
    
    # # Creating Creatures
    # while len(creatures) < number_of_creature:
    #     x_position = random.randint(0,lim_x)
    #     y_position = random.randint(0,lim_y)
    #     creature_energy = random.randint(5,25)
    #     sensor_radius = random.randint(2,7)
    #     creature = Creature(x_position,y_position,creature_energy,sensor_radius,world,"A")
        
    #     # Listing of all Creatures
    #     creature_coordinates = [(c.x, c.y) for c in creatures]
        
    #     # Check for existing Creatures
    #     if (creature.x, creature.y) not in creature_coordinates:
    #         creatures.append(creature)
    #         logger.info(f"Creature with X: {creature.x} and Y: {creature.y} and energy: {creature.energy} created!")
    #         i += 1
    
    # Simulation
    while not dead:
        
        # Shuffle of Creatures
        random.shuffle(creatures)
        
        for creature in creatures:
            if creature.energy > 0:
                creature.move()
                
                # Check for Food
                for food in world.food:           
                    if creature.x == food.x and creature.y == food.y:
                        creature.eat(food)
                        world.food.remove(food)
                        logger.info("Food eaten")
                        #break
                
                # Check for death and last creature
                if creature.energy == 0 and len(creatures) == 1:
                    creature.death()
                    creatures.remove(creature)
                    next_generation.append(creature)
                    logger.info("All Creatures died")
                    dead = True
                
                # Check for death
                elif creature.energy == 0:
                    # Last three creatures will be added to next generation
                    if len(creatures) <= 2:
                        next_generation.append(creature)
                    
                    # Death of Creature
                    creature.death()
                    creatures.remove(creature)                    
                    logger.info("Creature died")
                
                # Debug actual position and energy
                logger.info(creature.x, creature.y, creature.energy)
    
    return next_generation