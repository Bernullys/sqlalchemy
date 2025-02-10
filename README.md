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
