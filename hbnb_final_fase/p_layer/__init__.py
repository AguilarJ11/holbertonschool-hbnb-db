from hbnb_final_fase.p_layer.dataManager import DataManager
from hbnb_final_fase.p_layer.db_manager import Db_manager
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

# Carga el entorno desde el archivo .env
load_dotenv()
# Lee el entorno si seleccionamos si va ser una presistencia d ebase de datos o de archivos
persistence = os.getenv('PERSISTENCE')
database_url = os.getenv('DATABASE_URL')
# Si la presistencia es db pero la DATABASE_URL no esta definida entre sqllite y postgresql
if persistence == 'db' and not database_url:
    raise ValueError("DATABASE_URL no está definida en el archivo .env")
# Crear el motor de SQLAlchemy solo si la persistencia es 'db'
if persistence == 'db':
    engine = create_engine(database_url, pool_pre_ping=True)
    D_manager = Db_manager()
    print("Data base persistence")
else:
    print("File persistence")
    D_manager = DataManager()   
