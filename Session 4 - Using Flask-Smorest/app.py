from flask import Flask, request
from resources.item import blp as ItemBlueprint
from resources.store import blp as StoreBlueprint
from flask_smorest import Api


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

# REGISTER THE BLUEPRINTS THAT WE CREATED
# Create an API - This activates the settings that we have created above
api = Api(app)
api.register_blueprint(ItemBlueprint)
api.register_blueprint(StoreBlueprint)

# Run the flask web app
if __name__ == '__main__':
    app.run(debug=True)