from operator import or_
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker # se importa el operador and
from sqlalchemy import or_

# se importa la clase(s) del 
# archivo genera_tablas
from genera_tablas import *

# se importa información del archivo configuracion
from configuracion import cadena_base_datos
# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()


print("Parroquias que tienen establecimientos únicamente en la jornada Matutina y Vespertina") 

parroquias = session.query(Parroquia).join(Establecimiento).filter(or_(Establecimiento.jornada.like("%Matut%"), 
Establecimiento.jornada.like("%Vesper%"))).all()

for s in parroquias:
    print("%s" % (s))
    print("---------")

print("Los cantones que tiene establecimientos como número de estudiantes tales como: 448, 450, 451, 454, 458, 459")

cantones = session.query(Canton).join(Parroquia, Establecimiento).filter(or_(Establecimiento.numEstudiantes == 448, 
    Establecimiento.numEstudiantes == 450,
    Establecimiento.numEstudiantes == 451,
    Establecimiento.numEstudiantes == 454, 
    Establecimiento.numEstudiantes == 458,
    Establecimiento.numEstudiantes == 459)).all()

for c in cantones:
    print("%s" % (s))
    print("---------")