from sqlalchemy import Table, Column, Integer, String, create_engine, MetaData, insert, select

# Create an SQLite database file
engine = create_engine("sqlite:///step1_1.db", echo=True)  # echo=True prints SQL queries
# Metadata stores table definitions
metadata = MetaData()

# Define a users table
users = Table(
    "users", metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(50)),
    Column("age", Integer)
)
# Create the table in the database
metadata.create_all(engine)

# Insert a user into the table
with engine.connect() as conn:
    conn.execute(insert(users), {"name": "Alice", "age": 25})
    conn.commit()  # Save changes

# Select all users
with engine.connect() as conn:
    result = conn.execute(select(users))
    for row in result:
        print(row)  # Output: (1, 'Alice', 25)