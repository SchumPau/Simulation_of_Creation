import dataclasses

from typing import List

from classes.Food import Food
from classes.Creature import Creature

@dataclasses.dataclass
class World:
    max_x: int
    max_y: int
    food = List[Food]
    creatures = List[Creature]
    
    def __post_init__(self):
        self.food = []
        self.creatures = []
    
    def nearby_food(self, x, y, radius):
        nearby_food = [f for f in self.food if abs(f.x - x) <= radius and abs(f.y - y) <= radius]
        return sorted(nearby_food, key=lambda f: abs(f.x - x) + abs(f.y - y))