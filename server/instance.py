from flask import Flask, Blueprint
from flask_restplus import Api
from collections.abc import MutableMapping

class Server():
    def __init__(self, ):
        self.app = Flask(__name__)
        self.blueprint = Blueprint('api', __name__, url_prefix='/api')
        self.api = Api(self.blueprint, doc='/doc/', title='Minha API REST')
        self.app.register_blueprint(self.blueprint)

        # DB
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
        self.app.config['PROPAGATE_EXCEPTIONS'] = True
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        
        self.book_ns = self.book_ns()

    def book_ns(self, ):
        return self.api.namespace('book', description='book related operations', path='/')

    def run(self, ):
        self.app.run(
            port=5000,
            debug=True,
            host='0.0.0.0'
        )

server = Server()