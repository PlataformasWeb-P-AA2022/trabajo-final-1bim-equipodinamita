from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# se importa la clase(s) del 
# archivo genera_tablas
from genera_tablas import Provincia, Canton
# se importa información del archivo configuracion
from configuracion import cadena_base_datos
# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

provincias = [] 

def removeDuplicates(lst):  
    return list(set([i for i in lst]))


with open ('../data/Listado-Instituciones-Educativas.csv', 'r',encoding="utf8") as archivo:
    next(archivo, None)

    for linea in archivo:
        linea = linea.split('|')
        provincias.append((linea[2], linea[3]))

prov = removeDuplicates(provincias)

for p in prov:
    session.add(Provincia(codigo=p[0],nombre=p[1] ))
session.commit()




