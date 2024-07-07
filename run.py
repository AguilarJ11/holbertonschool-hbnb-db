#!/usr/bin/python3

from hbnb_final_fase import create_app, db
from config import create_db, env_name, persistence

"""
Crea una app de flask ya configurada con sus extenciones, y rutas.
Crea todas las tablas definidas previamente con mi modelo 'db'
"""

app = create_app()

if persistence == 'db' and env_name == 'development':
    print("----------------")
    print("Db inicializated")
    print("----------------")
    create_db(app, db)

if __name__ == "__main__":
    app.run(debug=app.config['DEBUG'])