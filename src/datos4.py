from operator import and_
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker # se importa el operador and
from sqlalchemy import or_ 


# se importa la clase(s) del 
# archivo genera_tablas
from genera_tablas import Canton, Provincia, Parroquia, Establecimiento

# se importa información del archivo configuracion
from configuracion import cadena_base_datos
# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

print("Los establecimientos ordenados por nombre de parroquia que tengan más de 40 profesores y la cadena Educación regular en tipo de educación.") 

establecimientos = session.query(Establecimiento, Parroquia).join(Parroquia)\
    .filter(and_(Establecimiento.numDocentes >40, Establecimiento.tipoEducacion.like('Educación regular')))\
        .order_by(Parroquia.nombre).all()

for s in establecimientos:
    print("%s" % (s))
    print("---------")

print("Todos los establecimientos ordenados por sostenimiento y tengan código de distrito 11D04.")

establecimientos2 = session.query(Establecimiento).filter(Establecimiento.codDistrito.like('11D04')).order_by(Establecimiento.sostenimiento)

for s in establecimientos2:
    print("%s" % (s))
    print("---------")