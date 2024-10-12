from marshmallow import Schema, fields

# WHEN CREATING ONE TO MANY OR MANY TO MANY.
# WE SHOULD ALWAYS CREATE SEPARATE SCHEMAS FOR THE ENTITY ITSELF AND ANOTHER SCHEMA FOR THE ENTITY WITH A RELATIONSHIP

# PLAIN = IT DOES NOT DEAL WITH ANY RELATIONSHIP
class PlainStoreSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.Str(required=True)

class PlainItemSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.Str(required=True)
    price = fields.Float(required=True)

class ItemUpdateSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str()
    price = fields.Float()

    store_id = fields.Integer()


# NEW SCHEMAS
# StoreSchema - id, name, items
class StoreSchema(PlainStoreSchema):
    items = fields.List(fields.Nested(PlainItemSchema), dump_only=True)
    

# ItemSchema - id, name, price
class ItemSchema(PlainItemSchema):
    store_id = fields.Int(required=True)
    store = fields.Nested(PlainStoreSchema, dump_only=True)

#################################



