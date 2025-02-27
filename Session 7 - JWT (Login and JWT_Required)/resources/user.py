from flask.views import MethodView
from flask_smorest import Blueprint, abort
from passlib.hash import pbkdf2_sha256
from flask_jwt_extended import create_access_token, jwt_required, get_jwt

from db import db
from models.user import UserModel
from schemas import UserSchema
from sqlalchemy.exc import SQLAlchemyError

blp = Blueprint("users", __name__, description="Operations on users endpoint.")

'''
'/register'  - POST   (accepts username and password)

'/user/<id>' - GET    (get user)      - TEMPORARY (for testing only)
'/user/<id>' - DELETE (delete user)   - TEMPORARY (for testing only)

'/login' - POST
'''

@blp.route("/login")
class UserLogin(MethodView):
    @blp.arguments(UserSchema)
    def post(self, req_body):
        user = UserModel.query.filter(
            UserModel.username == req_body["username"]
        ).first()

        if user:
            if pbkdf2_sha256.verify(req_body["password"], user.password):
                access_token = create_access_token(identity=user.id)
                return {"access_token": access_token}
            else:
                abort(400, message="Wrong password.")
        else:
            abort(400, message="User does not exist yet.")

@blp.route("/register")
class UserRegister(MethodView):
    @blp.arguments(UserSchema)
    def post(self, user_req_body):
        if UserModel.query.filter(UserModel.username == user_req_body["username"]).first():
            abort(409, message="A user with that username already exists.")

        user = UserModel(
            username=user_req_body["username"], 
            password=pbkdf2_sha256.hash(user_req_body["password"])
        )
        try:
            db.session.add(user)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occured while creating a new user.")
        
        return {"message": "User registered successfully."}, 201

@blp.route("/user/<int:user_id>")
class User(MethodView):
    @blp.response(200, UserSchema)
    def get(self, user_id):
        user = UserModel.query.get_or_404(user_id)
        return user

    def delete(self, user_id):
        user = UserModel.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()

        return {"message": "User deleted"}, 200
    
@blp.route("/my-info")
class UserInfo(MethodView):
    @jwt_required()
    @blp.response(200, UserSchema)
    def get(self):
        user = UserModel.query.get_or_404(get_jwt()["sub"])
        return user


# LOGIN -> JWT -> Identity/Subject 
# ID FROM JWT
# facebook.com/home