import dataclasses
from typing import List
from sqlalchemy import create_engine, insert, Connection
from decouple import config
import logging
import coloredlogs

from classes.Food import Food
from classes.Simulation import Simulation
from database.models import World as WorldModel

logger = logging.getLogger(__name__)
coloredlogs.install(level='INFO', logger=logger, fmt='[%(asctime)s] %(levelname)s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

@dataclasses.dataclass
class World:
    max_x: int
    max_y: int
    food = List[Food]
    simulation: Simulation
    existing_food: list
    database_id: int = None
    connection: Connection = None
    
    def __post_init__(self):
        self.food = self.existing_food
        
        # read environment variables
        user = config("DB_USER")
        password = config("DB_PASSWORD")
        host = config("DB_HOST")

        engine = create_engine(f"mysql+mysqlconnector://{user}:{password}@{host}:3306/simulation_of_creation")
        conn = engine.connect()
        self.connection = conn
        
        # insert into database
        stmt = insert(WorldModel).values(width=self.max_x, height=self.max_y, simulation_id=self.simulation.database_id)
        result = self.connection.execute(stmt)
        self.connection.commit()
        self.database_id = result.inserted_primary_key[0]
        logger.debug(f"Result of insert into world database: {result.inserted_primary_key}")
        logger.info(f"World with width: {self.max_x} and height: {self.max_y} created!")
    
    def nearby_food(self, x, y, radius):
        nearby_food = [f for f in self.food if abs(f.x - x) <= radius and abs(f.y - y) <= radius]
        return sorted(nearby_food, key=lambda f: abs(f.x - x) + abs(f.y - y))
    
    def set_remaining_food(self, remaining_food):
        stmt = WorldModel.update().where(WorldModel.id == self.database_id).values(remaining_food=remaining_food)
        self.connection.execute(stmt)
        self.connection.commit()
        logger.info(f"Remaining food updated to {remaining_food} in world with id {self.database_id}")