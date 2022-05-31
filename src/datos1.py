from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker # se importa el operador and

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


print("Consulta 1 \n Todos los establecimientos que pertenecen al Código División Política Administrativa Parroquia con valor 110553")

establecimientos1 = session.query(Establecimiento, Parroquia).join(Parroquia).filter(Parroquia.codigo.like('110553')).all()

for s in establecimientos1:
    print("%s" % (s))
    print("---------")


print("Consulta 2 \n Todos los establecimientos de la provincia del oro")

establecimientos2 = session.query(Establecimiento, Parroquia, Canton, Provincia).join(Establecimiento.parroquia, Parroquia.canton, Canton.provincia).filter(Provincia.nombre.like('EL ORO')).all()


for s in establecimientos2:
    print("%s" % (s))
    print("---------")

print("Consulta 3 \n Todos los establecimientos de la Portovelo")

establecimientos3 = session.query(Establecimiento, Parroquia, Canton, Provincia).join(Establecimiento.parroquia, Parroquia.canton, Canton.provincia).filter(Canton.nombre.like('PORTOVELO')).all()


for s in establecimientos3:
    print("%s" % (s))
    print("---------")

print("Consulta 4 \n Todos los establecimientos de la Zamora")

establecimientos4 = session.query(Establecimiento, Parroquia, Canton, Provincia).join(Establecimiento.parroquia, Parroquia.canton, Canton.provincia).filter(Canton.nombre.like('ZAMORA')).all()


for s in establecimientos4:
    print("%s" % (s))
    print("---------")




