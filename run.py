#!/usr/bin/python3

from hbnb_final_fase import create_app, db

"""
Crea una app de flask ya configurada con sus extenciones, y rutas.
Crea todas las tablas definidas previamente con mi modelo 'db'
"""

app = create_app()
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=app.config['DEBUG'])