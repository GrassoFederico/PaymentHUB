# Init Database

# Importa le dipendenze

from config import server, user, password, database
from sqlalchemy import create_engine, text
from init_orm import Base

# Istanzo l'engine

engine = create_engine("mysql://" + user + ":" + password + "@" + server + ":3306/" + database)

# Crea il database

print("\nInizializzo il database...")

Base.metadata.create_all(engine)