# sqlalchemy
SQLAlchemy

SQLAlchemy is a Python SQL toolkit and Object Relational Mapper (ORM) that allows you to interact with databases using Python code instead of writing raw SQL queries. It has two main components:
1. Core – Provides a SQL expression language to work with databases.
2. ORM (Object Relational Mapper) – Maps Python classes to database tables.

Lesson 1: Installing and Setting Up SQLAlchemy
    Step 1: Install SQLAlchemy
        pip install sqlalchemy
        pip install sqlalchemy[asyncio] asyncpg # If you're planning to use an async database like PostgreSQL.
    Step 2: Creating a Simple Database with SQLAlchemy Core
        Define a database connection:
            from sqlalchemy import create_engine, MetaData
            # Create an SQLite database file
            engine = create_engine("sqlite:///example.db", echo=True)  # echo=True prints SQL queries
            # Metadata stores table definitions
            metadata = MetaData()
        Define a table:
            from sqlalchemy import Table, Column, Integer, String
            # Define a users table
            users = Table(
                "users", metadata,
                Column("id", Integer, primary_key=True),
                Column("name", String(50)),
                Column("age", Integer)
            )
            # Create the table in the database
            metadata.create_all(engine)
    Step 3: Insert and Query Data
        Insert Data:
            from sqlalchemy import insert
            # Insert a user into the table
            with engine.connect() as conn:
                conn.execute(insert(users), {"name": "Alice", "age": 25})
                conn.commit()  # Save changes
        Query data:
            from sqlalchemy import select
            # Select all users
            with engine.connect() as conn:
                result = conn.execute(select(users))
                for row in result:
                    print(row)  # Output: (1, 'Alice', 25)

Lesson 2: SQLAlchemy ORM (Object Relational Mapper) - Defining Models and Interacting with a Database
    Step 1: Setting up SQLAlchemy ORM.
        The ORM allows us to define database tables as Python classes and interact with them as objects.
        from sqlalchemy import create_engine
        from sqlalchemy.orm import declarative_base, sessionmaker
    Step 2: Creating a Database and ORM Model.
        Unlike SQLAlchemy Core, where we defined tables manually, in ORM, we use Python classes to define tables.
        Define a Database connection:
            from sqlalchemy import create_engine
            from sqlalchemy.orm import declarative_base, sessionmaker
            # Create a database engine
            engine = create_engine("sqlite:///example.db", echo=True)
            # Create a Base class for ORM models
            Base = declarative_base()
            # Create a Session factory
            SessionLocal = sessionmaker(bind=engine)
        Define a Table as a Python Class (Model):
            from sqlalchemy import Column, Integer, String
            class User(Base):
                __tablename__ = "users"

                id = Column(Integer, primary_key=True, index=True)
                name = Column(String(50), nullable=False)
                age = Column(Integer)

            # Create tables in the database
            Base.metadata.create_all(engine)
            # This User class represents a table in the database.
    Step 3: Adding and Querying Data Using ORM.
        Now, let's insert data and query it using ORM.
        Insert Data:
            # Create a session
            session = SessionLocal()

            # Create a new user
            new_user = User(name="Alice", age=25)

            # Add and commit to the database
            session.add(new_user)
            session.commit()
        Query Data:
            # Retrieve all users
            users = session.query(User).all()
            for user in users:
                print(user.id, user.name, user.age)  # Output: 1 Alice 25

    Notes:
        A session in SQLAlchemy ORM is like a middleman between your Python code and the database. It handles:
            Connection management – Opens and closes database connections automatically.
            Transaction control – Groups multiple operations into a single transaction.
            Query execution – Helps retrieve and manipulate data using Python objects.