import dataclasses
from typing import List
from sqlalchemy import create_engine, insert, Connection
from decouple import config
import logging
import coloredlogs

from database.models import Simulation as SimulationModel

logger = logging.getLogger(__name__)
coloredlogs.install(level='INFO', logger=logger, fmt='[%(asctime)s] %(levelname)s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

@dataclasses.dataclass
class Simulation:
    database_id: int = None
    connection: Connection = None
    
    def __post_init__(self):
        # read environment variables
        user = config("DB_USER")
        password = config("DB_PASSWORD")
        host = config("DB_HOST")

        engine = create_engine(f"mysql+mysqlconnector://{user}:{password}@{host}:3306/simulation_of_creation")
        conn = engine.connect()
        self.connection = conn
        
        # insert into database
        stmt = insert(SimulationModel).values()
        result = self.connection.execute(stmt)
        self.connection.commit()
        self.database_id = result.inserted_primary_key[0]
        logger.debug(f"Result of insert into simulation database: {result.inserted_primary_key}")
        logger.info(f"Simulation created!")