import os

basedir = os.path.abspath(os.path.dirname(__file__))

# Tu clave secreta
SECRET_KEY = 'mi-clave-secreta-super-segura-para-reposteria'

# Base de datos SQLite local
SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "app.db")
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Flask-WTF flag for CSRF
CSRF_ENABLED = True

# App Builder globals
APP_NAME = "Repostería App"

# Autenticación basada en Base de Datos (1 = AUTH_DB)
AUTH_TYPE = 1

# Idioma por defecto
BABEL_DEFAULT_LOCALE = "es"
BABEL_DEFAULT_FOLDER = "translations"

LANGUAGES = {
    "es": {"flag": "es", "name": "Spanish"},
    "en": {"flag": "gb", "name": "English"},
}

# Configuración de archivos y subidas
UPLOAD_FOLDER = basedir + "/app/static/uploads/"
IMG_UPLOAD_FOLDER = basedir + "/app/static/uploads/"
IMG_UPLOAD_URL = "/static/uploads/"