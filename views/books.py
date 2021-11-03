from flask import request
from flask_restx import Resource, Namespace

from implemented import book_service

book_ns = Namespace('books')


@book_ns.route('/')
class BooksView(Resource):
    def get(self):
        books = book_service.get_all()
        res = []
        for s in books:
            sm_d = s.__dict__
            # грязный хак чтобы не перебирать поля так как здесь нет сериализации при помощи marshmallow
            del sm_d['_sa_instance_state']
            res.append(s.__dict__)

        return res, 200

    def post(self):
        req_json = request.json
        ent = book_service.create(req_json)
        return "", 201, {"location": f"/books/{ent.id}"}


@book_ns.route('/<int:bid>')
class BookView(Resource):
    def get(self, bid):
        book = book_service.get_one(bid)
        sm_d = book.__dict__
        # грязный хак чтобы не перебирать поля так как здесь нет сериализации при помощи marshmallow
        del sm_d['_sa_instance_state']
        return sm_d, 200

    def put(self, bid):
        req_json = request.json
        req_json["id"] = bid
        book_service.update(req_json)
        return "", 204

    def delete(self, bid):
        book_service.delete(bid)
        return "", 204
