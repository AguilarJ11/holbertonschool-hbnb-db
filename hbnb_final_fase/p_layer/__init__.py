from hbnb_final_fase.p_layer.dataManager import DataManager
from hbnb_final_fase.p_layer.db_manager import Db_manager
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv('app.env')
persistence = os.getenv('PERSISTENCE')
database_type = os.getenv('DATABASE_TYPE')
database_url = os.getenv('DATABASE_URL')

if persistence == 'db':
    print(f"{database_type} db persistence")
    engine = create_engine(database_url, pool_pre_ping=True)  
    D_manager = Db_manager()
elif persistence == 'file':
    print("File persistence")
    D_manager = DataManager()   
