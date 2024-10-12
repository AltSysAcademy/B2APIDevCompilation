from flask import Flask, request
from db import stores, items
from uuid import uuid4

# Create a web server using flask
app = Flask(__name__)

# First Endpoint
# GET Request - /store
@app.get("/store")
def get_all_store():
    return list(stores.values()), 200

# Second Endpoint
# POST Request - /store
@app.post("/store")
def add_new_store():
    new_store_data = request.get_json()

    store_id = uuid4().hex

    if "name" in new_store_data:
        for store in list(stores.values()):
            if store["name"] == new_store_data["name"]:
                return {"message": "Store name already exists."}, 400


        new_store = {
            "name": new_store_data["name"],
            "id": store_id
        }
        stores.update({store_id: new_store})

        return new_store, 201
    else:
        return {"message": "The key 'name' must be in the request body"}, 400

# Third Endpoint
# GET request - /store/<store_id>
@app.get("/store/<string:store_id>")
def get_specific_store(store_id):
    if store_id in stores:
        return stores[store_id], 200
    
    return {"message":'Store ID not found'}, 404

################
# CREATE ENDPOINTS FOR DATA MODEL 'item'

# Fourth Endpoint
@app.get("/item")
def get_all_item():
    return list(items.values()), 200

@app.post("/item")
def create_item():
    new_item_data = request.get_json()

    if "name" in new_item_data and "price" in new_item_data and "store_id" in new_item_data:

        for item in list(items.values()):
            if (item["name"] == new_item_data["name"]) and (item["store_id"] == new_item_data["store_id"]):
                return {"message": "Item name already exists."}, 400
    
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
        
        return {"message": "Store ID not found."}, 404
    else:
        return {"message": "The keys 'name', 'price', and 'store_id' should be in the request body."}

@app.get('/item/<string:item_id>')
def get_specific_item(item_id):
    if item_id in items:
        return items[item_id]
    return {"message": "Item ID does not exist."}

## ENDPOINT FOR DELETING ITEMS
@app.delete('/item/<string:item_id>')
def delete_specific_item(item_id):
    if item_id in items:
        del items[item_id]
        return {"message": "Item successfully deleted."}, 200
    return {"message": "Item ID does not exist."}, 400

# PUT Request - Idempotency
# 1. If we updated data but the data does not yet exist, we could create the data from the request provided
# 2. Change only what we have to.

@app.put('/item/<string:item_id>')
def edit_specific_item(item_id):
    # Get the req body
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
            return {"message": "Item does not exist."}, 404
    return {"message": "Either 'name' or 'price' should be in the request body."}, 400

# Run the flask web app
if __name__ == '__main__':
    app.run(debug=True)