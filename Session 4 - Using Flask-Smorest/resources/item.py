from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask import request
from db import stores, items
from uuid import uuid4

blp = Blueprint("items", __name__, description="Operations on items endpoint.")

@blp.route("/items/<string:item_id>")
class Item(MethodView):
    def get(self, item_id):
        if item_id in items:
            return items[item_id]
        abort(404, message="Item ID does not exist.")

    def delete(self, item_id):
        if item_id in items:
            del items[item_id]
            return {"message": "Item successfully deleted."}, 200
        abort(400, message="Item ID does not exist.")

    # WHEN YOU HAVE REQ BODY AND URL SEGMENT AT THE SAME TIME:
    # REQUEST BODY ALWAYS COMES FIRST
    # FOLLOWED BY THE URL SEGMENT
    def put(self, item_id):
        item_update_data = request.get_json()
        if "name" in item_update_data or "price" in item_update_data:
            # If the item exists
            if item_id in items:
                # Get the item
                item = items[item_id]

                item |= item_update_data

                # Return item
                return item, 200
            else:
                abort(404, message="Item does not exist.")
        abort(400, message="Either 'name' or 'price' should be in the request body.")

@blp.route("/items")
class ItemList(MethodView):
    def get(self):
        return list(items.values()), 200
    
    def post(self):
        new_item_data = request.get_json()
        if "name" in new_item_data and "price" in new_item_data and "store_id" in new_item_data:

            for item in list(items.values()):
                if (item["name"] == new_item_data["name"]) and (item["store_id"] == new_item_data["store_id"]):
                    abort(400, message="Item name already exists.")
        
            if new_item_data["store_id"] in stores:
                item_id = uuid4().hex

                new_item = {
                    "id": item_id,
                    "name": new_item_data["name"],
                    "price": new_item_data["price"],
                    "store_id": new_item_data["store_id"]
                }
                items.update({item_id: new_item})

                return new_item, 201
            
            abort(404, message="Store ID not found.")
        else:
            abort(400, message="The keys 'name', 'price', and 'store_id' should be in the request body.")