from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import stores, items
from uuid import uuid4
from schemas import ItemSchema, ItemUpdateSchema

blp = Blueprint("items", __name__, description="Operations on items endpoint.")

@blp.route("/items/<string:item_id>")
class Item(MethodView):
    # Adds response to the API Documentation
    # To serves as a data validation for our response
    @blp.response(200, ItemSchema)
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
    @blp.arguments(ItemUpdateSchema)
    @blp.response(200, ItemUpdateSchema)
    def put(self, item_update_data, item_id):
        if item_id in items:
            item = items[item_id]
            item |= item_update_data

            return item, 200
        else:
            abort(404, message="Item does not exist.")

@blp.route("/items")
class ItemList(MethodView):
    @blp.response(200, ItemSchema(many=True))
    def get(self):
        return items.values()
    
    @blp.arguments(ItemSchema)
    @blp.response(201, ItemSchema)
    def post(self, new_item_data):
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

            return new_item
        
        abort(404, message="Store ID not found.")