import dataclasses
import random

from classes.World import World
from classes.Food import Food

@dataclasses.dataclass
class Creature:
    x: int
    y: int
    energy: int
    senor_radius: int
    world: World
    type: str
    
    def move(self):
        # check for nearby food
        nearby_food = self.world.nearby_food(self.x, self.y, self.senor_radius)
        if nearby_food:
            food = nearby_food[0]
            if self.x < food.x:
                self.x += 1
            elif self.x > food.x:
                self.x -= 1
            elif self.y < food.y:
                self.y += 1
            elif self.y > food.y:
                self.y -= 1
            self.energy -= 1
        else:
            self.move_random()
    
    def move_random(self):
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