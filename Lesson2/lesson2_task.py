from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# Create a database engine
engine = create_engine("sqlite:///lesson2_task.db", echo=True)

# Create a Base class for ORM models
Base = declarative_base()

# Create a Session factory
SessionLocal = sessionmaker(bind=engine)

# Define a Table as a Python Class (Model)
class Book(Base):
    __tablename__ = "books"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50), nullable=False)
    author = Column(String(32), nullable=False)

# Create tables in the database
Base.metadata.create_all(engine)

#Insert Data:
# Create a session
session = SessionLocal()

# Create books
books_list = [
    Book(title="Harry Potter I", author="Merelic Street"),
    Book(title="Harry Potter II", author="Merelic Street")
]

# Add and commit to the database
session.add_all(books_list)
session.commit()

# Close session
session.close()

#Query Data:
books = session.query(Book).all()
for book in books:
    print(book.id, book.title, book.author)