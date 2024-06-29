from hbnb_final_fase.p_layer.dataManager import DataManager
from hbnb_final_fase.p_layer.db_manager import Db_manager
import os

if os.getenv('PERSISTENCE') == 'db':
    print("Data base persistence")
    D_manager = Db_manager()
else:
    print("File persistence")
    D_manager = DataManager()   
