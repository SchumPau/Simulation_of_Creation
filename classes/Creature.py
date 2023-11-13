import dataclasses
import random
from sqlalchemy import create_engine, insert, Connection
from decouple import config
import logging
import coloredlogs

from classes.World import World
from classes.Food import Food
from database.models import Creature as CreatureModel
from database.models import Log as LogModel

logger = logging.getLogger(__name__)
coloredlogs.install(level='DEBUG', logger=logger, fmt='[%(asctime)s] %(levelname)s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

@dataclasses.dataclass
class Creature:
    x: int
    y: int
    energy: int
    sensor_radius: int
    world: World
    type: str
    database_id: int = None
    connection: Connection = None
    log_data: list = dataclasses.field(default_factory=list, init=False)
    
    def __post_init__(self):
        # read environment variables
        user = config("DB_USER")
        password = config("DB_PASSWORD")
        host = config("DB_HOST")

        engine = create_engine(f"mysql+mysqlconnector://{user}:{password}@{host}:3306/{user}")
        conn = engine.connect()
        self.connection = conn
        
        # insert into database
        stmt = insert(CreatureModel).values(start_x=self.x, start_y=self.y, start_energy=self.energy, sensor_radius=self.sensor_radius, type=self.type, world_id=self.world.database_id)
        result = self.connection.execute(stmt)
        self.connection.commit()
        self.database_id = result.inserted_primary_key[0]
        logger.debug(f"Result of insert into creatures database: {result.inserted_primary_key}")
        logger.info(f"Creature of type {self.type} at X: {self.x} and Y: {self.y} and energy: {self.energy} and sensor_radius {self.sensor_radius} created!")
    
    def move(self):
        # check for nearby food
        nearby_food = self.world.nearby_food(self.x, self.y, self.sensor_radius)
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
            
        # insert into log
        self.log_data.append({
            'creature_id': self.database_id,
            'x': self.x,
            'y': self.y,
            'energy': self.energy
        })
    
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
        
    def eat(self, food: Food):
        self.energy += food.energy_provided
        
    def death(self):
        # insert into database
        stmt = insert(LogModel).values(self.log_data)
        result = self.connection.execute(stmt)
        self.connection.commit()
        logger.debug(f"Result of batch insert into log database: {result.inserted_primary_key}")
        self.log_data = []