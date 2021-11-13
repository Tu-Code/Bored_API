# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from os import path
# from flask_login import LoginManager
# from flask_migrate import Migrate

# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'Jesus'
# app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# db = SQLAlchemy( app )
# DB_NAME = "database.db"
# migrate = Migrate()

# from .models import User

# db.create_all()

# # migrate.init_app(app, db)
    
# from .views import *
# from .auth import *

# from .controllers import *




#     login_manager = LoginManager()
#     login_manager.login_view = 'auth.login'
#     login_manager.init_app(app)

#     @login_manager.user_loader
#     def load_user(id):
#         return User.query.get(int(id))
        
#     return app


# def create_database(app):
#     if not path.exists('foodie/' + DB_NAME):
#         db.create_all(app=app)
#         print('Created Database!')

