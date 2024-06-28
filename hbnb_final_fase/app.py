from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///development.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Para desactivar advertencias de modificaciones de seguimiento
db = SQLAlchemy(app)

if __name__ == '__main__':
    app.run(debug=True)