# pylint: disable=C0111,W0702
# - [C0111] WARNING: missing module, class docstrings.
# - [W0702] WARNING: No exception type(s) specified.
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel


class ItemList(Resource):
    def get(self):
        return {'items': [item.json() for item in ItemModel.find_all()]}


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'price',
        type=float,
        required=True,
        help="This field cannot be blank."
    )
    parser.add_argument(
        'store_id',
        type=float,
        required=True,
        help="Every item needs a store id."
    )

    @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_name(name)
        if not item:
            return {'message': 'Item not found'}, 404

        return item.json(), 200

    def post(self, name):
        if ItemModel.find_by_name(name):
            return {
                'message': f"An item with name '{name}' already exists."}, 400

        data = Item.parser.parse_args()
        item = ItemModel(name, **data)
        try:
            item.save_to_db()
        except:
            return {'message': 'An error occurred when inserting the item.'}, 500

        return item.json(), 201

    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if not item:
            return {'message': f"An item with name '{name}' does not exist."}, 400

        ItemModel.delete_from_db(item)
        return {'message': 'Item deleted'}, 200

    def put(self, name):
        data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name)

        if item:
            item.price = data['price']
        else:
            item = ItemModel(name, **data)

        item.save_to_db()
        return item.json(), 200
