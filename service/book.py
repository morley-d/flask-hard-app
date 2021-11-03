from dao.book import BookDAO


class BookService:
    def __init__(self, dao: BookDAO):
        self.dao = dao

    def get_one(self, bid):
        return self.dao.get_one(bid)

    def get_all(self):
        return self.dao.get_all()
    
    def create(self, book_d):
        return self.dao.create(book_d)

    def update(self, book_d):
        self.dao.update(book_d)
        return self.dao

    def delete(self, rid):
        self.dao.delete(rid)