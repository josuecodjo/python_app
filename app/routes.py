# custom
from app import app
from flask import Flask, jsonify, abort, make_response, request

# app = Flask(__name__)

books = [
    {
        "id": 1,
        "title": "CS50",
        "description": "Intro to CS and art of programming!",
        "author": "Havard",
        "borrowed": False
    },
    {
        "id": 2,
        "title": "Python 101",
        "description": "little python code book.",
        "author": "Will",
        "borrowed": False
    }
]


@app.route('/')
def web_root():
    return 'Web App with Python Flask!'
@app.route('/data')
def web_data():
    return 'Hello here is my data!'
@app.route('/home')
def web_home():
    return 'Hello here is my Home folder!'
@app.route('/init')
def web_init():
    return 'Hello here is my init web page!'
@app.route("/square") # localhost/square?number=8
def square():
    number = int(request.args.get("number", 0))
    return str(number ** 2)
    
# get and jsonify the data
@app.route("/bookapi/books")
def get_books():
    """ function to get all books """
    return jsonify({"Books": books})


# get book by provided 'id'
@app.route("/bookapi/books/<int:book_id>", methods=['GET'])
def get_by_id(book_id):
    book = [book for book in books if book['id'] == book_id]
    if len(book) == 0:
        abort(404)
    return jsonify({"Book": books[0]})

#error handling
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({"error": "book not found!"}), 404)

# app.run(host='0.0.0.0', port=30100)