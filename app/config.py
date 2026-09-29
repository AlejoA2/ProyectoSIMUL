import os

class config:
    SQLACLHEMY_DATABASE_URI = os.getenv(
        'DATABASE_URL',
    "mysql+pymysql://inventory_user:inventory_password@db:3306/inventory_db"
    )

    #lo usamos para evitar el envio de informacion de seguimiento de modificaciones a la base de datos
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    #clave utilizada para firmar los tokens JWT
    JWT_SECRET_KEY = os.getenv(
        'JWT_SECRET_KEY',
        'super-secret-key-produccion'
        )
    #3600 segundos eso es igual a 1 hora, es el tiempo de expiracion del token
    JWT_ACCESS_TOKEN_EXPIRES = 3600