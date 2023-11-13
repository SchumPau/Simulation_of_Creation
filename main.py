from classes.Creature import Creature
from classes.World import World
from classes.Food import Food
from functions.death_simulation import simulation

i = 0
dead = False
next_generation = []

while not dead:
    
    next_generation = simulation(lim_x=100,lim_y=100,number_of_food=100,number_of_creature=10)
    i += 1
    
print(f"Simulation finished after {i} iterations")
