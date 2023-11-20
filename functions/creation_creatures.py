from classes.Creature import Creature
from classes.World import World
from classes.Food import Food
import random
import logging
import coloredlogs
from typing import List

logger = logging.getLogger(__name__)
coloredlogs.install(level='INFO', logger=logger, fmt='[%(asctime)s] %(levelname)s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

def create_creature(number_of_creatures: int, world: World, old_generation: List[Creature]):
    
    creatures = []
    lim_x = world.max_x
    lim_y = world.max_y
    
    if old_generation == []:
        
        while len(creatures) < number_of_creatures:
            x_position = random.randint(0,lim_x)
            y_position = random.randint(0,lim_y)
            creature_energy = random.randint(5,25)
            sensor_radius = random.randint(2,7)
            creature = Creature(x_position,y_position,creature_energy,sensor_radius,world,"A")
            
            # Listing of all Creatures
            creature_coordinates = [(c.x, c.y) for c in creatures]
            
            # Check for existing Creatures
            if (creature.x, creature.y) not in creature_coordinates:
                creatures.append(creature)
    
    else:
        
        parent_1 = random.choice(old_generation)
        parent_2 = random.choice(old_generation)
        parent_3 = random.choice(old_generation)
        parent_4 = random.choice(old_generation)
        logger.debug(f"Parent 1: {parent_1}")
        logger.debug(f"Parent 2: {parent_2}")
        logger.debug(f"Parent 3: {parent_3}")
        logger.debug(f"Parent 4: {parent_4}")
        
        # Childs from parent 1 and 2
        number_of_creatures_created = 0
        while number_of_creatures_created != 5:
            x_position = random.randint(0,lim_x)
            y_position = random.randint(0,lim_y)
            creature_energy = random.randint(min(parent_1.start_energy,parent_2.start_energy), max(parent_1.start_energy,parent_2.start_energy)) + random.randint(-2,2)
            sensor_radius = random.randint(min(parent_1.sensor_radius,parent_2.sensor_radius), max(parent_1.sensor_radius,parent_2.sensor_radius)) + random.randint(-5,5)
            # No negative values
            if creature_energy < 0:
                creature_energy = 1
            if sensor_radius < 0:
                sensor_radius = 1
            creature = Creature(x_position,y_position,creature_energy,sensor_radius,world,"A")
            logger.debug(f"Child {number_of_creatures_created} from Parent 1+2 created")
            
            # Listing of all Creatures
            creature_coordinates = [(c.x, c.y) for c in creatures]
            
            # Check for existing Creatures
            if (creature.x, creature.y) not in creature_coordinates:
                creatures.append(creature)
                number_of_creatures_created += 1
        
        # Childs from parent 3 and 4
        number_of_creatures_created = 0
        while number_of_creatures_created != 5:
            x_position = random.randint(0,lim_x)
            y_position = random.randint(0,lim_y)
            creature_energy = random.randint(min(parent_3.start_energy,parent_4.start_energy), max(parent_3.start_energy,parent_4.start_energy)) + random.randint(-2,2)
            sensor_radius = random.randint(min(parent_3.sensor_radius,parent_4.sensor_radius), max(parent_3.sensor_radius,parent_4.sensor_radius)) + random.randint(-5,5)
            # No negative values
            if creature_energy < 0:
                creature_energy = 1
            if sensor_radius < 0:
                sensor_radius = 1
            creature = Creature(x_position,y_position,creature_energy,sensor_radius,world,"A")
            logger.debug(f"Child {number_of_creatures_created} from Parent 3+4 created")
            
            # Listing of all Creatures
            creature_coordinates = [(c.x, c.y) for c in creatures]
            
            # Check for existing Creatures
            if (creature.x, creature.y) not in creature_coordinates:
                creatures.append(creature)
                number_of_creatures_created += 1
            
    return creatures