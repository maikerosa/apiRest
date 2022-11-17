from flask import request
from flask_restplus import Resource, fields

from models.book import BookModel
from schemas.book import BookSchema

from server.instance import server

book_ns = server.book_ns
book_schema = BookSchema()
book_list_schema = BookSchema(many=True)

ITEM_NOT_FOUND = 'Nada encontrado'

item = book_ns.model('Book', {
    'title': fields.String(required=True, description='Titulo do livro'),
    'pages': fields.Integer(default=0, description='Numero de paginas')
})

class Book(Resource):
    def get(self, id):
        book = BookModel.find_by_id(id)
        if book:
            return book_schema.dump(book), 200
        return {'message': ITEM_NOT_FOUND}, 404


class BookList(Resource):
    def get(self):
        return {'books': book_list_schema.dump(BookModel.find_all())}, 200

    @book_ns.expect(item)
    @book_ns.doc('create_book')
    def post(self):
        book_json = request.get_json()
        book_data = book_schema.load(book_json)
       
        if BookModel.find_by_title(book_data.title):
            return {'message': f'Um livro com o titulo {book_data.title} ja existe.'}, 400
        else:
            book = BookModel(**book_data)
            return book_schema.dump(book), 201

class BookDelete(Resource):
    def delete(self, id):
        book = BookModel.find_by_id(id)
        if book:
            book.delete_from_db()
            return {'message': 'Item deletado'}, 200
        return {'message': ITEM_NOT_FOUND}, 404