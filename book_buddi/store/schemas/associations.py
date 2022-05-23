from sqlalchemy import Column, ForeignKey 
from database import Base

class BookByShelf(Base):
    __tablename__="BOOK_BY_SHELF"
    book = Column(ForeignKey("BOOK.id"))
    shelf = Column(ForeignKey("SHELF.id"))


class ComicByShelf(Base):
    __tablename__="COMIC_BY_SHELF"
    comic = Column(ForeignKey("COMIC_BOOK.id"))
    shelf = Column(ForeignKey("SHELF.id"))


class BookByAuthor(Base):
    __tablename__="BOOK_BY_AUTHOR"
    book = Column(ForeignKey("BOOK.id"))
    author = Column(ForeignKey("AUTHOR.id"))


class ComicByAuthor(Base):
    __tablename__="COMIC_BY_AUTHOR"
    comic = Column(ForeignKey("COMIC_BOOK.id"))
    author = Column(ForeignKey("AUTHOR.id"))

class ComicByIllustrator(Base):
    __tablename__="COMIC_BY_ILLUSTRATOR"
    comic = Column(ForeignKey("COMIC_BOOK.id"))
    illustrator = Column(ForeignKey("ILLUSTRATOR.id"))

class BookByGenre(Base):
    __tablename__="BOOK_BY_GENRE"
    book = Column(ForeignKey("BOOK.id"))
    genre = Column(ForeignKey("GENRE.id"))


class ComicByGenre(Base):
    __tablename__="COMIC_BY_GENRE"
    comic = Column(ForeignKey("COMIC.id"))
    genre = Column(ForeignKey("GENRE.id"))






