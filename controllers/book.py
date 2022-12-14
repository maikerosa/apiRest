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
   
class BookCreate(Resource):
    @book_ns.expect(item)
    @book_ns.doc('create_book')
    def post(self):
        book_json = request.get_json()
        book_data = book_schema.load(book_json)
       
        if BookModel.find_by_title(book_data.title):
            return {'message': f'Um livro com o titulo {book_data.title} ja existe.'}, 400
        else:
            book = BookModel(title=book_data.title, pages=book_data.pages)
            try:
                book.save_to_db()
            except:
                return {'message': 'Ocorreu um erro ao salvar o livro.'}, 500
            return book_schema.dump(book), 201
    

class BookUpdate(Resource):
    @book_ns.expect(item)
    @book_ns.doc('update_book')
    def put(self, id):
        book_data = BookModel.find_by_id(id)
        book_json = request.get_json()

        book_data.pages = book_json['pages']
        book_data.title = book_json['title']

        book_data.save_to_db()
        return book_schema.dump(book_data), 200

class BookDelete(Resource):
    @book_ns.doc('delete_book')
    @book_ns.response(204, 'Book deleted')
    def delete(self, id):
        book_data = BookModel.find_by_id(id)
        if book_data:
            book_data.delete_from_db()
            return {'message': 'Item deleted.'}, 200
        return {'message': ITEM_NOT_FOUND}, 404