import dataclasses
import random

from classes.World import World

@dataclasses.dataclass
class Creature:
    x: int
    y: int
    energy: int
    senor_radius: int
    world: World
    type: str
    
    def move(self):
        while True:
            direction = random.randint(0, 3)
            if direction == 0 and self.x > 0:
                self.x -= 1
                break
            elif direction == 1 and self.x < self.world.max_x - 1:
                self.x += 1
                break
            elif direction == 2 and self.y > 0:
                self.y -= 1
                break
            elif direction == 3 and self.y < self.world.max_y - 1:
                self.y += 1
                break
        self.energy -= 1
        
    def eat(self, food):
        self.energy += food.energy_provided
        self.world.remove_food(food)