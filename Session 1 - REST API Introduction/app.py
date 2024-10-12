from flask import Flask
from flask import request

# Create a web server using flask
app = Flask(__name__)

# DATA MODEL
# Ano yung gagamitin mong data
# [Dictionary]
stores = [
    {
        "name": "Nino Store", 
        "items": [
            {
                "name": "Chair",
                "price": 19.99
            },
            {
                "name": "Laptop",
                "price": 1009.99
            }
        ]
    },
    {
        "name": "Altis Store", 
        "items": [
            {
                "name": "Chair",
                "price": 19.99
            },
            {
                "name": "Sofa",
                "price": 1009.99
            }
        ]
    }
]


# First Endpoint
# GET Request - /store
@app.get("/store")
def get_all_store():
    return stores, 200

# Second Endpoint
# POST Request - /store
@app.post("/store")
def add_new_store():
    req_body = request.get_json()

    new_store = {
        "name": req_body["store_name"],
        "items": []
    }
    stores.append(new_store)

    return new_store, 201

# Third Endpoint
# GET request - /store/<STORE_NAME>
@app.get("/store/<string:store_name>")
def get_specific_store(store_name):
    for store in stores:
        if store["name"] == store_name:
            return store
    
    return {"message":'Store not found'}, 404


# Fourth Endpoints
@app.get('/store/<string:store_name>/item')
def get_item_in_store(store_name):
    for store in stores:
        if store["name"] == store_name:
            return store["items"]
    
    return {"message": "Store not found"}, 404

# Fifth Endpoint
@app.post('/store/<string:store_name>/item')
def create_item_in_store(store_name):
    request_body = request.get_json()

    for store in stores:
        if store["name"] == store_name:
            new_item = {
                "name": request_body["name"],
                "price": request_body["price"]
            }

            store["items"].append(new_item)
            
            return new_item, 201

    return {"message": "Store not found"}, 404





# Run the flask web app
if __name__ == '__main__':
    app.run(debug=True)