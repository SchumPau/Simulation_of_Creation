from sqlalchemy import create_engine, Column, Integer, Text, ForeignKey, text
from sqlalchemy.orm import declarative_base, relationship
from decouple import config

# read environment variables
user = config("DB_USER")
password = config("DB_PASSWORD")
host = config("DB_HOST")

engine = create_engine(f"mysql+mysqlconnector://{user}:{password}@{host}:3306/simulation_of_creation")
conn = engine.connect()
result = conn.execute(text("SHOW TABLES"))
print(result.fetchall())

Base = declarative_base()

class World(Base):
    __tablename__ = "worlds"
    id = Column(Integer, primary_key=True, autoincrement=True)
    width = Column(Integer)
    height = Column(Integer)
    remaining_food = Column(Integer)
    simulation_id = Column(Integer, ForeignKey("simulations.id"))
    creatures = relationship("Creature", back_populates="world")
    
class Creature(Base):
    __tablename__ = "creatures"
    id = Column(Integer, primary_key=True, autoincrement=True)
    start_x = Column(Integer)
    start_y = Column(Integer)
    start_energy = Column(Integer)
    sensor_radius = Column(Integer)
    type = Column(Text)
    world_id = Column(Integer, ForeignKey("worlds.id"))
    world = relationship("World", back_populates="creatures")
    
class Log(Base):
    __tablename__ = "logs"
    id = Column(Integer, primary_key=True, autoincrement=True)
    creature_id = Column(Integer, ForeignKey("creatures.id"))
    creature = relationship("Creature")
    x = Column(Integer)
    y = Column(Integer)
    energy = Column(Integer)
    
class Simulation(Base):
    __tablename__ = "simulations"
    id = Column(Integer, primary_key=True, autoincrement=True)
    world_id = Column(Integer, ForeignKey("worlds.id"))
    world = relationship("World")
    
Base.metadata.create_all(engine)