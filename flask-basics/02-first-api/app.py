"""" First Flask REST API"""
# pylint: disable=C0111
# - [C0111] is a warning when missing function docstrings.
from flask import Flask, jsonify, request, render_template

# -------- SERVER SETUP --------
app = Flask(__name__)  # pylint: disable=invalid-name

# -------- DATA --------
stores = [  # pylint: disable=invalid-name
    {
        'name': 'My Wonderful Store',
        'items': [
            {'name': 'Laptop', 'price': 1699.95},
            {'name': 'TV', 'price': 1100.00},
        ]
    }
]


# -------- ROUTES --------
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)


@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message': 'store not found'})


@app.route('/store')
def get_stores():
    return jsonify({'stores': stores})


@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message': 'store not found'})


@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items': store['items']})
    return jsonify({'message': 'store not found'})


# -------- START SERVER --------
app.run(port=5000)
