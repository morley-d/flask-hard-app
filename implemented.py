from dao.book import BookDAO
from dao.review import ReviewDAO
from service.book import BookService
from service.review import ReviewService
from setup_db import db

book_dao = BookDAO(db.session)
book_service = BookService(dao=book_dao)

review_dao = ReviewDAO(db.session)
review_service = ReviewService(dao=review_dao)