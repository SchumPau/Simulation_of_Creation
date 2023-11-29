from classes.Creature import Creature
from classes.World import World
from classes.Food import Food
from classes.Simulation import Simulation

from functions.death_simulation import simulation
from functions.creation_creatures import create_creature

next_generation = []
old_generation = []
remaining_food = []
first_round = True
lim_x = 100
lim_y = 100
number_of_food = 100
number_of_creatures = 10

sim = Simulation()

for round in range(100):
    
    world = World(lim_x, lim_y, sim, remaining_food)    
    
    next_generation = create_creature(number_of_creatures, world, old_generation)
    
    old_generation, remaining_food = simulation(number_of_food, number_of_creatures, first_round, next_generation, world)
    
    world.set_remaining_food(len(remaining_food))
    # print(result)
    
    first_round = False
    
print(f"Simulation finished after {round} iterations")
