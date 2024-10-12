from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import stores
from uuid import uuid4
from schemas import StoreSchema
# CREATE A BLUEPRINT FOR THIS RESOURCE
# FORMAT: Blueprint(name, __name__, description="Put description here.")
# This would be put on the API Documentation
blp = Blueprint("stores", __name__, description="Operations on stores endpoint.")

# MethodView - Allows us to group different HTTP Methods in a single class
# Class - Specific Stores
@blp.route("/store/<string:store_id>")
class Store(MethodView):
    # GET REQUEST
    # blp.response - EXPECTED OUTPUT
    @blp.response(200, StoreSchema)
    def get(self, store_id):
        if store_id in stores:
            # ID, NAME
            return stores[store_id]

        abort(404, message="Store ID not found")
    
    # DELETE REQUEST
    def delete(self, store_id):
        if store_id in stores:
            del stores[store_id]
            return {"message": "Store Deleted."}, 200
        else:
            abort(404, message="Store not found.")

@blp.route("/store")
class StoreList(MethodView):
    @blp.response(200, StoreSchema(many=True))
    def get(self):
        return stores.values()
    
    # blp.argument - anong klaseng request body ang tatanggapin
    # REQ_BODY(JSON) -> MARSHMALLOW(STORESCHEMA) -> POST
    @blp.arguments(StoreSchema)
    @blp.response(201, StoreSchema)
    def post(self, new_store_data):

        
        store_id = uuid4().hex

        for store in list(stores.values()):
            if store["name"] == new_store_data["name"]:
                abort(400, message="Store name already exists.")

        new_store = {
            "name": new_store_data["name"],
            "id": store_id
        }
        stores.update({store_id: new_store})

        return new_store
    