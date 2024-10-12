from marshmallow import Schema, fields

class StoreSchema(Schema):
    # dump_only - It is not required on the post part, but when we try to retrieve, it would show up.
    # GET REQUEST - LALABAS SI ID
    # POST REQUEST - DI NATIN NEED MAGLAGAY NG ID
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)

class ItemSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    price = fields.Float(required=True)
    store_id = fields.Str(required=True)

class ItemUpdateSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str()
    price = fields.Float()