from xmlrpc.client import DateTime
from sqlalchemy import Column, ForeignKey, String, Date, DateTime, Float, Boolean, Integer
from sqlalchemy.orm import relationship
from database import Base

class Book(Base):
    __tablename__ = "BOOK"
    id = Column(primary_key=True)

    type = Column(ForeignKey("TYPE.id"))
    ownership_stat = Column(ForeignKey("OWNERSHIP_STATUS.id"))

    title = Column(String, nullable=False)
    publication_yr = Column(Date)
    rating = Column(Float)
    rental_stat = Column(Boolean)

    shelves = relationship("Shelf", secondary='BOOK_BY_SHELF')
    authors = relationship("Author", secondary='BOOK_BY_AUTHOR')
    genres = relationship("Genre", secondary='BOOK_BY_GENRE')


class ComicBook(Base):
    __tablename__ = "COMIC_BOOK"
    id = Column(primary_key=True)

    type = Column(ForeignKey("TYPE.id"))
    ownership_stat = Column(ForeignKey("OWNERSHIP_STATUS.id"))

    title = Column(String, nullable=False)
    publisher = Column(String, nullable=False)
    protagonist = Column(String)
    entry_number = Column(Integer)
    publication_yr = Column(Date)
    rating = Column(Float)
    rental_stat = Column(Boolean)

    shelves = relationship("Shelf", secondary='BOOK_BY_SHELF')
    authors = relationship("Author", secondary='BOOK_BY_AUTHOR')
    illustrators = relationship("Illustrator", secondary='BOOK_BY_ILLUSTRATOR')
    genres = relationship("Genre", secondary='BOOK_BY_GENRE')


class Journal(Base):
    __tablename__ = "JOURNAL"
    id = Column(primary_key=True)

    type = Column(ForeignKey("TYPE.id"))

    description = Column(String, nullable=False)
    date_added = Column(DateTime)
    date_finished = Column(DateTime)
    status_notes = Column(String)

class Shelf(Base):
    __tablename__= "SHELF"
    id = Column(primary_key=True)

    name = Column(String, nullable=False)
    description = Column(String, nullable=False)

    books = relationship(Book, secondary='BOOK_BY_SHELF')
    comics = relationship(ComicBook, secondary='COMIC_BY_SHELF')


class Author(Base):
    __tablename__="AUTHOR"
    id = Column(primary_key=True)
    
    name = Column(String, nullable=False)

    books = relationship(Book, secondary='BOOK_BY_AUTHOR')
    comics = relationship(ComicBook, secondary='COMIC_BY_AUTHOR')


class Illustrator(Base):
    __tablename__="ILLUSTRATOR"
    id = Column(primary_key=True)
    
    name = Column(String, nullable=False)

    comics = relationship(ComicBook, secondary='COMIC_BY_ILLUSTRATOR')


class Genre(Base):
    __tablename__="GENRE"
    id = Column(primary_key=True)
    
    name = Column(String, nullable=False)

    books = relationship(Book, secondary='BOOK_BY_GENRE')
    comics = relationship(ComicBook, secondary='COMIC_BY_GENRE')

class Type(Base):
    __tablename__="TYPE"
    id = Column(primary_key=True)
    
    name = Column(String, nullable=False)

    books = relationship(Book, backref='TYPE')
    comics = relationship(ComicBook, backref='TYPE')
    journals = relationship(Journal, backref='TYPE')


class OwnershipStatus(Base):
    __tablename__="OWNERSHIP_STATUS"
    id = Column(primary_key=True)

    status = Column(String, nullable=False)
    description = Column(String, nullable=False)

    books = relationship(Book, backref='TYPE')
    comics = relationship(ComicBook, backref='TYPE')
