from classes.Creature import Creature
from classes.World import World
from classes.Food import Food
from functions.death_simulation import simulation

i = 0
dead = False
while not dead:
    dead = simulation()
    i += 1
    
print(f"Simulation finished after {i} iterations")
