from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# se importa la clase(s) del 
# archivo genera_tablas
from genera_tablas import Establecimiento,Parroquia
# se importa información del archivo configuracion
from configuracion import cadena_base_datos
# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

establecimientos = [] 

def removeDuplicates(lst):  
    return list(set([i for i in lst]))


with open ('../data/Listado-Instituciones-Educativas.csv', 'r',encoding="utf8") as archivo:
    next(archivo, None)

    for linea in archivo:
        linea = linea.split('|')
        establecimientos.append((linea[0],linea[1],linea[8],linea[9],linea[10],linea[11],linea[12],linea[13], linea[14], linea[15].replace('\n',''), linea[6]))


print(establecimientos)

for e in establecimientos:
    parr = session.query(Parroquia).filter_by(codigo=e[10]).one()

    session.add(Establecimiento(codigoAMIE=e[0], nombre=e[1], codDistrito=e[2],sostenimiento=e[3], tipoEducacion=e[4], modalidad=e[5], jornada=e[6], acceso=e[7],numEstudiantes=int(e[8]), numDocentes=int(e[9]), parroquia = parr))
session.commit()




