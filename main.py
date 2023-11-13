from classes.Creature import Creature
from classes.World import World
from classes.Food import Food
from functions.death_simulation import simulation
from functions.Creation_Creatures import Create_Creature

i = 0
dead = False
next_generation = []
old_generation = []
first_round = True
lim_x=100
lim_y=100
number_of_food=100
number_of_creature=10

while not dead:
    
    world = World(lim_x, lim_y)    
    
    old_generation = Create_Creature(number_of_creature,lim_x,lim_y,world,next_generation)
    
    next_generation = simulation(lim_x,lim_y,number_of_food,number_of_creature,first_round,old_generation,world)
    
    first_round = False
    i += 1
    if i == 10:
        dead = True
    
print(f"Simulation finished after {i} iterations")
