from flask import jsonify
from marshmallow import ValidationError

from ma import ma
from db import db
from controllers.book import Book, BookList, BookUpdate, BookCreate, BookDelete

from server.instance import server

api = server.api
app = server.app

@app.before_first_request
def create_tables():
    db.create_all()

api.add_resource(Book, '/book/<int:id>')
api.add_resource(BookList, '/books')
api.add_resource(BookCreate, '/books/create')
api.add_resource(BookUpdate, '/books/update/<int:id>')
api.add_resource(BookDelete, '/books/delete/<int:id>')

if __name__ == '__main__':
    db.init_app(app)
    ma.init_app(app)
    server.run()