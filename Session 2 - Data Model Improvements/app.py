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

    new_store = {
        "name": new_store_data["name"],
        "id": store_id
    }
    stores.update({store_id: new_store})

    return new_store, 201

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


# Run the flask web app
if __name__ == '__main__':
    app.run(debug=True)