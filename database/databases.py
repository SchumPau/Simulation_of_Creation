from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, Session

engine = create_engine("mysql:///d03ea7f0:oehFeJGRVUxvY7xP2FsL@w01aea79.kasserver.com", echo=True)