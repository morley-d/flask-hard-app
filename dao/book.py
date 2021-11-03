from dao.model.book import Book


class BookDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, bid):
        return self.session.query(Book).get(bid)

    def get_all(self):
        return self.session.query(Book).all()

    def create(self, book_d):
        ent = Book(**book_d)
        self.session.add(ent)
        self.session.commit()
        return ent

    def delete(self, rid):
        book = self.get_one(rid)
        self.session.delete(book)
        self.session.commit()

    def update(self, book_d):
        book = self.get_one(book_d.get("id"))
        book.user = book_d.get("user")
        book.rating = book_d.get("rating")
        book.book_id = book_d.get("book_id")

        self.session.add(book)
        self.session.commit()
