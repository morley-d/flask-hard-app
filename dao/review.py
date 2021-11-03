from dao.model.review import Review


class ReviewDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, bid):
        return self.session.query(Review).get(bid)

    def get_all(self):
        return self.session.query(Review).all()

    def create(self, review_d):
        ent = Review(**review_d)
        self.session.add(ent)
        self.session.commit()
        return ent

    def delete(self, rid):
        review = self.get_one(rid)
        self.session.delete(review)
        self.session.commit()

    def update(self, review_d):
        review = self.get_one(review_d.get("id"))
        review.user = review_d.get("user")
        review.rating = review_d.get("rating")
        review.book_id = review_d.get("book_id")

        self.session.add(review)
        self.session.commit()
