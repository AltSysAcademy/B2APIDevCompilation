from flask import Flask, request
from resources.item import blp as ItemBlueprint
from resources.store import blp as StoreBlueprint
from resources.tag import blp as TagBlueprint
from resources.user import blp as UserBlueprint
from flask_smorest import Api
from flask_jwt_extended import JWTManager


## Import all models FOR THE SQLALCHEMY TO GENERATE TABLES 
from models.item_tags import ItemsTags
from models.item import ItemModel
from models.store import StoreModel
from models.tag import TagModel
from models.user import UserModel

from db import db

# Create a web server using flask
app = Flask(__name__)

# Setup the Blueprints and the API Documentation
app.config["PROPAGATE_EXCEPTIONS"] = True

# Title that would show up in the documentation
app.config["API_TITLE"] = "Stores REST API"
app.config["API_VERSION"] = "v1"

# OPENAPI Setup
app.config["OPENAPI_VERSION"] = "3.1.0"
app.config["OPENAPI_URL_PREFIX"] = "/"

# Documentation Website Setup
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"

# Connect flask app to the database
db.init_app(app)

# Create the tables based on the models
with app.app_context():
    db.create_all()

api = Api(app)
api.register_blueprint(ItemBlueprint)
api.register_blueprint(StoreBlueprint)
api.register_blueprint(TagBlueprint)
api.register_blueprint(UserBlueprint)

app.config["JWT_SECRET_KEY"] = "132354456734573457754335648563456"
jwt = JWTManager(app)

# Run the flask web app
if __name__ == '__main__':
    app.run(debug=True)

# 132354456734573457754335648563456
'''
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcyNzY5OTY4OSwianRpIjoiNWUzNzFjNDUtNDM2ZC00YmFhLTlmZjEtZTdjNDM3MGFlNWE2IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6MSwibmJmIjoxNzI3Njk5Njg5LCJjc3JmIjoiN2NjYjBkODQtYTNkNC00ZmQyLWE4ODQtZTBlYjRkMzdjYTgxIiwiZXhwIjoxNzI3NzAwNTg5fQ.PFFC7jWgYx2QXI9TkWfEKX9mwruuKIsdfePtiNlTt38
'''


''' NinoDulay Signature
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcyNzY5OTY1NywianRpIjoiMDliMmI1YWUtOGY3OC00NjViLWI4ZTktM2UyMjM5ZGZmMzNlIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6MSwibmJmIjoxNzI3Njk5NjU3LCJjc3JmIjoiNjI3ZjNiYjMtYzM4Ny00N2U0LWIyOGUtZmZmYjAzZWIwODAwIiwiZXhwIjoxNzI3NzAwNTU3fQ.VaxK_4kA_pEKjW-smUgL2xrnmlW2Yhx6R-MldvviVog
'''