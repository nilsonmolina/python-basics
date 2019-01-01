# pylint: disable=C0111,W0702
# - [C0111] WARNING: missing module, class docstrings.
# - [W0702] WARNING: No exception type(s) specified.
from flask_restful import Resource
from models.store import StoreModel


class StoreList(Resource):
    def get(self):
        return {'items': [store.json() for store in StoreModel.find_all()]}


class Store(Resource):
    def get(self, name):
        store = StoreModel.find_by_name(name)
        if not store:
            return {'message': 'Store not found'}, 404
        return store.json(), 200

    def post(self, name):
        if StoreModel.find_by_name(name):
            return {'message': f"A store with name '{name}' already exists."}, 400
        store = StoreModel(name)
        try:
            store.save_to_db()
        except:
            return {'message': 'An error occurred when inserting the store.'}, 500
        return store.json(), 201

    def delete(self, name):
        store = StoreModel.find_by_name(name)
        if not store:
            return {'message': f"A store with name '{name}' does not exist."}, 400

        StoreModel.delete_from_db(store)
        return {'message': 'Store deleted'}, 200
