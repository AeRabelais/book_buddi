from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker 
from sqlalchemy.orm import declarative_base


engine = create_engine('sqlite:///./book_budi_db', echo=True)

Base = declarative_base()
Session = sessionmaker(bind=engine)


