"""" First Flask REST API"""
# pylint: disable=C0111,C0103
# - [C0111] is a warning when missing function docstrings.
# - [C0103] WARNING: constant names not UPPER_CASE style.
import datetime
from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from user import UserRegister  # pylint: disable=C0411
from item import Item, ItemList

# --------- SERVER SETUP ---------
app = Flask(__name__)
app.secret_key = 'my_secret'
api = Api(app)

app.config['JWT_AUTH_URL_RULE'] = '/auth'  # this is the default endpoint
jwt = JWT(app, authenticate, identity)  # creates new endpoint: /auth
app.config['JWT_EXPIRATION_DELTA'] = datetime.timedelta(seconds=1800)  # (default 5 min)

# --------- RESOURCES ---------
api.add_resource(ItemList, '/items')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(UserRegister, '/register')

# --------- START SERVER ---------
if __name__ == "__main__":  # will NOT run server if app.py is imported as package
    app.run(port=5000, debug=True)
