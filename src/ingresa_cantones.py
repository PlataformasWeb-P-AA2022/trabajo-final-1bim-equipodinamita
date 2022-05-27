from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# se importa la clase(s) del 
# archivo genera_tablas
from genera_tablas import Canton ,Provincia
# se importa información del archivo configuracion
from configuracion import cadena_base_datos
# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

cantones = [] 

def removeDuplicates(lst):  
    return list(set([i for i in lst]))


with open ('../data/Listado-Instituciones-Educativas.csv', 'r',encoding="utf8") as archivo:
    next(archivo, None)

    for linea in archivo:
        linea = linea.split('|')
        cantones.append((linea[4], linea[5], linea[2]))

cantones = removeDuplicates(cantones)

for c in cantones:
    prov = session.query(Provincia).filter_by(codigo=c[2]).one()\

    session.add(Canton(codigo=c[0],nombre=c[1],provincia = prov))
session.commit()




