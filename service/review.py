from dao.review import ReviewDAO


class ReviewService:
    def __init__(self, dao: ReviewDAO):
        self.dao = dao

    def get_one(self, bid):
        return self.dao.get_one(bid)

    def get_all(self):
        return self.dao.get_all()

    def create(self, review_d):
        return self.dao.create(review_d)

    def update(self, review_d):
        self.dao.update(review_d)
        return self.dao

    def delete(self, rid):
        self.dao.delete(rid)