from flask import Flask, jsonify
from flask import request
from flask import render_template

# create app from flask
app = Flask(__name__)

stores = [
    {
        "name": "My wonderful Stores",
        "items": [
            {
                "name": "My items",
                "price": 15.99
            }
        ]
    }
]


@app.route('/')
def home():
    names = ["a", "b", "c", "D"]
    return render_template("index.html", names=names)


# what  request it is  going to handle

# POST -  going to receive dataa
# GET - data needs to be sent

# POST /store  data: {name: }
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    # will return a string
    return jsonify(new_store)


# GET /store/<string:name>
@app.route('/store/<string:name>')
def get_store(name):
    # iterate over stores
    # if the store name matches return it
    for store in stores:
        if name == store['name']:
            return jsonify(store['name'])
    return jsonify({'message': 'store not found'})


@app.route('/store')
def get_stores():
    return jsonify({'stores': stores})


@app.route('/store/<string:name>/item', methods=['POST'])
def create_store_item(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
                 }
            store['items'].append(new_item)
            return jsonify(store)
    return jsonify({'message': 'store not found'})


@app.route('/store/<string:name>/items')
def get_store_item(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items': store['items']})
    return jsonify({'message': 'Requested item not found'})


app.run(port=5000)
