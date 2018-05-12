#!flask/bin/python
from flask import Flask, jsonify, make_response, request, abort

app = Flask(__name__)

books = [
    {
        'id': 1,
        'title': 'Dark Bane',
        'description': 'Trilogy of dark bane the wise', 
        'done': False
    },
    {
        'id': 2,
        'title': 'Ahsoka',
        'description': 'History of ahsoka after the clone wars and before rebels', 
        'done': True
    }
]

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': '404 Not found'}), 404)

@app.route('/api/books', methods=['GET'])
def get_book():
    return jsonify({'books': books})

@app.route('/api/books', methods=['POST'])
def create_book():
    if not request.json or not 'title' in request.json:
        print("Error not json, or not title in {}".format(request.json))
        abort(400)
    book = {
        'id': books[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    books.append(book)
    return jsonify({'book': book}), 201

if __name__ == '__main__':
    app.run(debug=True)