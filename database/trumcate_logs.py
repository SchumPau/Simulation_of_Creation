from sqlalchemy import create_engine, text
from decouple import config

# read environment variables
user = config("DB_USER")
password = config("DB_PASSWORD")
host = config("DB_HOST")

engine = create_engine(f"mysql+mysqlconnector://{user}:{password}@{host}:3306/simulation_of_creation")
conn = engine.connect()
result = conn.execute(text("TRUNCATE TABLE logs"))
print(result.fetchall())

