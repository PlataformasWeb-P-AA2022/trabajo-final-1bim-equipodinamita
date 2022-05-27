from contextlib import nullcontext
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import Column, Integer, String, ForeignKey

# se importa información del archivo configuracion
from configuracion import cadena_base_datos

# se genera en enlace al gestor de base de
# datos
engine = create_engine(cadena_base_datos)

Base = declarative_base()

# Ejemplo que representa la relación entre dos clases
# One to Many
# Un establecimiento tiene características propias.

class Provincia(Base):
    __tablename__ = 'provincia'
    id = Column(Integer, primary_key=True)
    codigo = Column(String(50))
    nombre = Column(String(100))
    # Mapea la relación entre las clases
    # Provincia puede acceder a los cantones asociados
    # por la llave foránea
    cantones = relationship("Canton", back_populates="provincia")

    def __repr__(self):
        return "Provincia: codigo=%s - nombre=%s "  % (
                          self.codigo, 
                          self.nombre)

# Un cantón pertence a un provincia.

class Canton(Base):
    __tablename__ = 'canton'
    id = Column(Integer, primary_key=True)
    codigo = Column(String(50))
    nombre = Column(String(100), nullable=False)
    # se agrega la columna provincia_id como ForeignKey
    provincia_id = Column(Integer, ForeignKey('provincia.id'))
    # Mapea la relación entre las clases
    # Canton puede acceder a las provincias asociados
    # por la llave foránea
    provincia = relationship("Provincia", back_populates="cantones")
    # Mapea la relación entre las clases
    # Canton puede acceder a las parroquias asociados
    # por la llave foránea
    parroquia = relationship("Parroquia", back_populates="canton")

    def __repr__(self):
        return "Canton: codigo=%s - nombre=%s " % (
                          self.codigo, 
                          self.nombre)

# Una parroquia pertence a un cantón.

class Parroquia(Base):
    __tablename__ = 'parroquia'
    id = Column(Integer, primary_key=True)
    codigo = Column(String(50))
    nombre = Column(String(100))
    # se agrega la columna canton_id como ForeignKey
    # se hace referencia al id de la entidad canton
    canton_id = Column(Integer, ForeignKey('canton.id'))
    # Mapea la relación entre las clases
    # Parroquia tiene una relación con Canton
    canton  = relationship("Canton", back_populates="parroquia")
    # Mapea la relación entre las clases
    # Parroquia puede acceder a los establecimientos asociados
    # por la llave foránea
    establecimiento  = relationship("Establecimiento", back_populates="parroquia")
    
    def __repr__(self):
        return "Parroquia: codigo=%s - nombre=%s " % (
                self.codigo, self.nombre)

# Un establecimiento pertenece a una parroquia.

class Establecimiento(Base):
    __tablename__ = 'establecimiento'
    id = Column(Integer, primary_key=True)
    codigoAMIE = Column(String(100))
    nombre = Column(String(100))
    codDistrito = Column(String(50))
    sostenimiento = Column(String(100))
    tipoEducacion = Column(String(100))
    modalidad = Column(String(50))
    jornada = Column(String(50))
    acceso = Column(String(50))
    numEstudiantes = Column(Integer)
    numDocentes = Column(Integer)
    # se agrega la columna parroquia_id como ForeignKey
    # se hace referencia al id de la entidad parroquia
    parroquia_id = Column(Integer, ForeignKey('parroquia.id'))
    # Mapea la relación entre las clases
    # Establecimiento tiene una relación con Parroquias
    parroquia = relationship("Parroquia", back_populates="establecimiento")

    
    def __repr__(self):
        return "Establecimiento: codigoAMIE=%s - nombre=%s - codDistrito=%s - sostenimiento=%s - tipoEducacion=%s - modalidad=%s - jornada=%s - acceso=%s - numEstudiantes=%d - numDocentes=%d " % (
                          self.codigoAMIE, 
                          self.nombre, 
                          self.codDistrito, 
                          self.sostenimiento,
                          self.tipoEducacion,
                          self.modalidad,
                          self.jornada,
                          self.acceso,
                          self.numEstudiantes,
                          self.numDocentes)

Base.metadata.create_all(engine)








