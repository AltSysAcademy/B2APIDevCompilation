from db import db

class StoreModel(db.Model):
    __tablename__ = "stores"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)

    # ItemModel.store would contain a StoreModel
    items = db.relationship("ItemModel", back_populates="store", lazy="dynamic", cascade="all, delete")

