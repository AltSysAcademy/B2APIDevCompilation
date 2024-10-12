from flask.views import MethodView
from flask import request
from flask_smorest import Blueprint, abort
from db import stores
from uuid import uuid4

# CREATE A BLUEPRINT FOR THIS RESOURCE
# FORMAT: Blueprint(name, __name__, description="Put description here.")
# This would be put on the API Documentation
blp = Blueprint("stores", __name__, description="Operations on stores endpoint.")


# MethodView - Allows us to group different HTTP Methods in a single class
# Class - Specific Stores
@blp.route("/store/<string:store_id>")
class Store(MethodView):
    # GET REQUEST
    def get(self, store_id):
        if store_id in stores:
            return stores[store_id], 200

        abort(404, message="Store ID not found")
    
    # DELETE REQUEST
    def delete(self, store_id):
        if store_id in stores:
            del stores[store_id]
            return {"message": "Store Deleted."}
        else:
            abort(404, message="Store not found.")

@blp.route("/store")
class StoreList(MethodView):
    def get(self):
        return list(stores.values()), 200
    
    # Second Parameter - Request Body
    def post(self):
        new_store_data = request.get_json()

        store_id = uuid4().hex

        if "name" in new_store_data:
            for store in list(stores.values()):
                if store["name"] == new_store_data["name"]:
                    abort(400, message="Store name already exists.")

            new_store = {
                "name": new_store_data["name"],
                "id": store_id
            }
            stores.update({store_id: new_store})

            return new_store, 201
        else:
            abort(400, message="The key 'name' must be in the request body")
    