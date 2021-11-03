from flask import request
from flask_restx import Resource, Namespace

from implemented import review_service

review_ns = Namespace('reviews')


@review_ns.route('/')
class ReviewsView(Resource):
    def get(self):
        reviews = review_service.get_all()
        res = []
        for s in reviews:
            sm_d = s.__dict__
            # грязный хак чтобы не перебирать поля так как здесь нет сериализации при помощи marshmallow
            del sm_d['_sa_instance_state']
            res.append(s.__dict__)

        return res, 200

    def post(self):
        req_json = request.json
        ent = review_service.create(req_json)
        return "", 201, {"location": f"/reviews/{ent.id}"}


@review_ns.route('/<int:rid>')
class ReviewView(Resource):
    def get(self, rid):
        review = review_service.get_one(rid)
        sm_d = review.__dict__
        # грязный хак чтобы не перебирать поля так как здесь нет сериализации при помощи marshmallow
        del sm_d['_sa_instance_state']
        return sm_d, 200

    def put(self, rid):
        req_json = request.json
        req_json["id"] = rid
        review_service.update(req_json)
        return "", 204

    def delete(self, rid):
        review_service.delete(rid)
        return "", 204
