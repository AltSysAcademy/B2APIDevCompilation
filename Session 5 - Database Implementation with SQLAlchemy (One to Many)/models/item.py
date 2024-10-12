from db import db

class ItemModel(db.Model):
    # Table Name
    __tablename__ = "items"

    # Create the fields(columns)
    id = db.Column(db.Integer, primary_key=True)    

    # null - empty (emptyable)
    name = db.Column(db.String(80), nullable=False, unique=True)

    price = db.Column(db.Float(precision=2))

    # unique = False - Repeatable
    store_id = db.Column(db.Integer, db.ForeignKey("stores.id"), unique=False, nullable=False)

    # In this relationship, we want this relationship to connect to the StoreModel(stores)
    store = db.relationship("StoreModel", back_populates="items")
