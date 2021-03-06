"""" First Flask REST API"""
# pylint: disable=C0111,C0103
# - [C0111] is a warning when missing function docstrings.
# - [C0103] WARNING: constant names not UPPER_CASE style.
import datetime
from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister, User
from resources.item import Item, ItemList
from resources.store import Store, StoreList

# --------- SERVER SETUP ---------
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPOGATE_EXCEPTIONS'] = True
app.secret_key = 'my_secret'
api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()


app.config['JWT_AUTH_URL_RULE'] = '/auth'
jwt = JWT(app, authenticate, identity)
app.config['JWT_EXPIRATION_DELTA'] = datetime.timedelta(seconds=1800)

# --------- RESOURCES ---------
api.add_resource(ItemList, '/items')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(StoreList, '/stores')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(UserRegister, '/register')
api.add_resource(User, '/user/<int:user_id>')

# --------- START SERVER ---------
if __name__ == "__main__":
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
