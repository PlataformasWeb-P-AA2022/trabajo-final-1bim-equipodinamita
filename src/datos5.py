from operator import and_
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker # se importa el operador and
from sqlalchemy import or_ 
from sqlalchemy import asc


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

print("Los establecimientos ordenados por número de estudiantes que tengan más de 100 profesores.")
establecimientos = session.query(Establecimiento).filter(Establecimiento.numDocentes > 100)\
    .order_by(asc(Establecimiento.numEstudiantes)).all()

for s in establecimientos:
    print("%s" % (s))
    print("---------")

print("\nLos establecimientos ordenados por número de profesores que tengan más de 100 profesores.")

establecimientos2 = session.query(Establecimiento).filter(Establecimiento.numDocentes > 100)\
    .order_by(asc(Establecimiento.numDocentes)).all()

for s in establecimientos2:
    print("%s" % (s))
    print("---------")