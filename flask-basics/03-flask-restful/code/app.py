"""" First Flask REST API"""
# pylint: disable=C0111,C0103
# - [C0111] is a warning when missing function docstrings.
# - [C0103] WARNING: constant names not UPPER_CASE style.
from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required
from security import authenticate, identity

# --------- SERVER SETUP ---------
app = Flask(__name__)
app.secret_key = 'my_secret'
api = Api(app)

jwt = JWT(app, authenticate, identity)  # creates new endpoint: /auth

# --------- IN-MEMORY DB ---------
items = []


# --------- RESOURCES ---------
class ItemList(Resource):
    def get(self):
        return {'items': items}


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'price',
        type=float,
        required=True,
        help="This field cannot be left blank!"
    )

    @jwt_required()
    def get(self, name):
        item = next(filter(lambda i: i['name'] == name, items), None)
        return {'item': item}, 200 if item else 404

    def post(self, name):
        if next(filter(lambda i: i['name'] == name, items), None):
            return {'message': f"An item with name '{name}' already exists."}, 400

        data = Item.parser.parse_args()
        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 201

    def delete(self, name):
        global items
        if not next(filter(lambda i: i['name'] == name, items), None):
            return {'message': f"An item with name '{name}' does not exist."}, 400

        items = [i for i in items if i['name'] != name]
        return {'message': 'Item deleted'}, 200

    def put(self, name):
        data = Item.parser.parse_args()

        item = next(filter(lambda i: i['name'] == name, items), None)
        if item is None:
            item = {'name': name, 'price': data['price']}
            items.append(item)
        else:
            item.update(data)
        return item


api.add_resource(ItemList, '/items')
api.add_resource(Item, '/item/<string:name>')

app.run(port=5000, debug=True)
