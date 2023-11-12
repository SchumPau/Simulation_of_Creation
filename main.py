from classes.Creature import Creature
from classes.World import World
from classes.Food import Food
from functions.death_simulation import simulation

i = 0
gegessen = False
while not gegessen:
    gegessen = simulation()
    i += 1
    
print(f"Simulation finished after {i} iterations")
