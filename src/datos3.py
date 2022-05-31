from operator import and_, or_
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker # se importa el operador and
from sqlalchemy import or_, and_


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


print("Los cantones que tiene establecimientos con 0 número de profesores, 5 profesores, 11 profesores")

cantones = session.query(Canton).join(Parroquia,Establecimiento)\
    .filter(or_(Establecimiento.numDocentes == 0 , Establecimiento.numDocentes == 5 , Establecimiento.numDocentes == 11)).all()

for s in cantones:
    print("%s" % (s))
    print("---------")

print("Los establecimientos que pertenecen a la parroquia Pindal con estudiantes mayores o iguales a 21")
establecimientos = session.query(Establecimiento, Parroquia).join(Parroquia)\
    .filter(and_(Parroquia.nombre.like('PINDAL'), Establecimiento.numEstudiantes >= 21))
    
for s in establecimientos:
    print("%s" % (s))
    print("---------")