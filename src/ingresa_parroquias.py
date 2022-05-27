from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# se importa la clase(s) del 
# archivo genera_tablas
from genera_tablas import Canton ,Parroquia
# se importa información del archivo configuracion
from configuracion import cadena_base_datos
# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

parroquias = [] 

def removeDuplicates(lst):  
    return list(set([i for i in lst]))


with open ('../data/Listado-Instituciones-Educativas.csv', 'r',encoding="utf8") as archivo:
    next(archivo, None)

    for linea in archivo:
        linea = linea.split('|')
        parroquias.append((linea[6], linea[7], linea[4]))

parroquias = removeDuplicates(parroquias)

for p in parroquias:
    c = session.query(Canton).filter_by(codigo=p[2]).one()

    session.add(Parroquia(codigo=p[0],nombre=p[1],canton = c))
session.commit()




