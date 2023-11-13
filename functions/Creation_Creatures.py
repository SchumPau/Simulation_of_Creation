from classes.Creature import Creature
from classes.World import World
from classes.Food import Food
import random
import logging
import coloredlogs

logger = logging.getLogger(__name__)
coloredlogs.install(level='DEBUG', logger=logger, fmt='[%(asctime)s] %(levelname)s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

def Create_Creature (number_of_creature,lim_x,lim_y,world,old_generation):
    
    creatures = []
    i = 0
    
    if old_generation == []:
        
        while len(creatures) < number_of_creature:
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
                logger.info(f"Creature with X: {creature.x} and Y: {creature.y} and energy: {creature.energy} created!")
                i += 1
    
    else:
        
        parent_1 = random.choice(old_generation)
        parent_2 = random.choice(old_generation)
        parent_3 = random.choice(old_generation)
        parent_4 = random.choice(old_generation)
        
        # Childs from parent 1 and 2
        while i != 5:
            x_position = random.randint(0,lim_x)
            y_position = random.randint(0,lim_y)
            creature_energy = random.randint(parent_1.energy,parent_2.energy)
            sensor_radius = random.randint(parent_1.sensor_radius,parent_2.sensor_radius)
            creature = Creature(x_position,y_position,creature_energy,sensor_radius,world,"A")
            
            # Listing of all Creatures
            creature_coordinates = [(c.x, c.y) for c in creatures]
            
            # Check for existing Creatures
            if (creature.x, creature.y) not in creature_coordinates:
                creatures.append(creature)
                logger.info(f"Creature with X: {creature.x} and Y: {creature.y} and energy: {creature.energy} created!")
                i += 1
        
        # Childs from parent 3 and 4
        while i != 5:
            x_position = random.randint(0,lim_x)
            y_position = random.randint(0,lim_y)
            creature_energy = random.randint(parent_3.energy,parent_4.energy)
            sensor_radius = random.randint(parent_3.sensor_radius,parent_4.sensor_radius)
            creature = Creature(x_position,y_position,creature_energy,sensor_radius,world,"A")
            
            # Listing of all Creatures
            creature_coordinates = [(c.x, c.y) for c in creatures]
            
            # Check for existing Creatures
            if (creature.x, creature.y) not in creature_coordinates:
                creatures.append(creature)
                logger.info(f"Creature with X: {creature.x} and Y: {creature.y} and energy: {creature.energy} created!")
                i += 1
        
        creatures = old_generation
            
    return creatures