from flask import Flask
from flask_jwt_extended import JWTManager

#importamos las referencias creadas
from app.extensions import db
from app.config import config

#manejos de rutas con blueprints



#
def create_app():
    app = Flask(
        __name__,
        static_folder='static',
        template_folder='templates'
    )

    #configuramos la app con los parametros de configuracion
    app.config.from_object(config)

    #inicializamos las extensiones con la app
    db.init_app(app)
    jwt = JWTManager(app)

    #registramos los blueprints
    with app.app_context():
        db.create_all()  # Crea las tablas en la base de datos si no existen

    return app