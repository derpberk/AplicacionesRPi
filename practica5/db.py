from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Punto de entrada a la bbdd
engine = create_engine('sqlite:///estacionamientos.db',
                       connect_args={'check_same_thread': False})

# Session - generador de sesiones con la bbdd
Session = sessionmaker(bind=engine)

# seesion - instancia de sesión con la bbdd
session = Session()

# Base - clase base del resto de clases que se crearan
# a partir del mapeo de las tablas en clases
Base = declarative_base()