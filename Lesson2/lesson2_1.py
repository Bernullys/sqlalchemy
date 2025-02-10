from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# Create a database engine
engine = create_engine("sqlite:///lesson2.db", echo=True)

# Create a Base class for ORM models
Base = declarative_base()

# Create a Session factory
SessionLocal = sessionmaker(bind=engine)

# Define a Table as a Python Class (Model)
class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    age = Column(Integer)

# Create tables in the database
Base.metadata.create_all(engine)

#Insert Data:
# Create a session
session = SessionLocal()

# Create a new user
new_user = User(name="Alice", age=25)

# Add and commit to the database
session.add(new_user)
session.commit()

session.close()

#Query Data:
# Retrieve all users
users = session.query(User).all()
for user in users:
    print(user.id, user.name, user.age)  # Output: 1 Alice 25