from flask import Flask, jsonify, abort, make_response, request

from version_1 import find_all, find_by_id, cl, find_by_parameter, find_by_name

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello, World!"


# http://127.0.0.1:5000/item/2
@app.route('/item/<int:item_id>', methods=['GET'])
def url_by_id(item_id):
    item = find_by_id(item_id)
    if item:
        return jsonify({'item': item})
    else:
        abort(404)


# curl -H "Content-Type: application/json" -X GET -d "{\"_id\":2}" http://127.0.0.1:5000/item/by_id
@app.route('/item/by_id', methods=['GET'])
def json_by_id():
    item_id = request.get_json()
    item = find_by_id(item_id['_id'])
    if item:
        return jsonify({'item': item})
    else:
        abort(404)


# curl -H "Content-Type: application/json" -X GET -d "{\"title\":\"sUS\"}" http://127.0.0.1:5000/item/by_title
@app.route('/item/by_title', methods=['GET'])
def json_by_title():
    item_title = request.get_json()
    item_list = find_by_name(item_title['title'])
    items = [i for i in item_list]
    if items:
        return jsonify({'item': items})
    else:
        abort(404)


# curl -H "Content-Type: application/json" -X GET -d "{\"param\":\"price\", \"value\": 100000, \"flag\": true}" http://127.0.0.1:5000/item/by_price
@app.route('/item/by_price', methods=['GET'])
def json_by_price():
    if not request.json or 'param' not in request.json:
        abort(400)
    json_dict = request.get_json()
    ls = find_by_parameter(param=json_dict['param'], value=json_dict['value'], flag=json_dict['flag'])
    # items = [i['title'] for i in ls]
    items = [i for i in ls]

    return jsonify({'items': items})


# curl -H "Content-Type: application/json" -X POST -d "{\"title\":\"Asus\", \"desc\":\"Gaming SuperBook\", \"parameters\":{\"RAM\":\"24GB\",\"GPU\":\"2080TI\",\"CPU\":\"i999\", \"price\":120000}}" http://127.0.0.1:5000/item
@app.route('/item', methods=['POST'])
def create_item():
    if not request.json or 'title' not in request.json:
        abort(400)
    id_gen = [i['_id'] for i in find_all()][-1] + 1
    json_dict = request.get_json()
    item = {
        '_id': id_gen,
        'title': json_dict['title'],
        'desc': json_dict['desc'],
        'parameters': [json_dict['parameters']]
    }
    cl.insert_one(item)
    return jsonify({'item': item}), 201


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': 'Bad request'}), 400)


if __name__ == '__main__':
    app.run(debug=True)
