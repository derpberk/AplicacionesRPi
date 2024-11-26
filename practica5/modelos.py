import db
from sqlalchemy import Column, Integer, String, Float, Date

# Los modelos son las clases que representan las tablas de bases de datos

class Garaje(db.Base):
    __tablename__ = "garaje"

    id = Column(Integer, primary_key=True)
    vehiculo_id = Column(String)
    n_plaza = Column(Integer)

    def __init__(self, id, vehiculo_id, n_plaza):
        self.id = id
        self.vehiculo_id = vehiculo_id
        self.n_plaza = n_plaza

class Vehiculo(db.Base):
    __tablename__ = "vehiculo"

    id = Column(Integer, primary_key=True)
    propietario_id = Column(Integer)
    tipo_id = Column(Integer)
    matricula = Column(String)
    marca = Column(String)
    modelo = Column(String)

    def __init__(self, propietario_id, tipo_id,
                 matricula, marca, modelo):

        self.propietario_id = propietario_id
        self.tipo_id = tipo_id
        self.matricula = matricula
        self.marca = marca
        self.modelo = modelo

