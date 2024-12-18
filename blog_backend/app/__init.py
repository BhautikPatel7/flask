from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
migrate = Migrate()

db = SQLAlchemy()
bcrypt = Bcrypt()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    migrate.init_app(app, db)
    # congigration
    app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///blog.db'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config['JWT_SECRET_KEY'] = "My_JWT_Screet_Key_Is_Not_Secure()"

    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    from .auth import auth
    app.register_blueprint(auth,url_prefix= "/auth")
    return app