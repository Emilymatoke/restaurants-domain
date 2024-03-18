import sqlite3

def create_tables():
    # Connect to SQLite database
    connection = sqlite3.connect("restaurant_reviews.db")
    cursor = connection.cursor()

    # Create tables
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS restaurants (
            id INTEGER PRIMARY KEY,
            name TEXT,
            price INTEGER
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY,
            first_name TEXT,
            last_name TEXT
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS reviews (
            id INTEGER PRIMARY KEY,
            restaurant_id INTEGER,
            customer_id INTEGER,
            star_rating INTEGER,
            FOREIGN KEY (restaurant_id) REFERENCES restaurants(id),
            FOREIGN KEY (customer_id) REFERENCES customers(id)
        )
    """)

    # Commit changes and close connection
    connection.commit()
    connection.close()

def insert_sample_data():
    # Connect to SQLite database
    connection = sqlite3.connect("restaurant_reviews.db")
    cursor = connection.cursor()

    # Insert sample data
    cursor.execute("INSERT INTO restaurants (name, price) VALUES (?, ?)", ("Pizza Inn", 3))
    cursor.execute("INSERT INTO restaurants (name, price) VALUES (?, ?)", ("Burger King", 4))

    cursor.execute("INSERT INTO customers (first_name, last_name) VALUES (?, ?)", ("Emily", "Matoke"))
    cursor.execute("INSERT INTO customers (first_name, last_name) VALUES (?, ?)", ("Brenda", "Ngugi"))

    cursor.execute("INSERT INTO reviews (restaurant_id, customer_id, star_rating) VALUES (?, ?, ?)", (1, 1, 5))
    cursor.execute("INSERT INTO reviews (restaurant_id, customer_id, star_rating) VALUES (?, ?, ?)", (2, 1, 4))
    cursor.execute("INSERT INTO reviews (restaurant_id, customer_id, star_rating) VALUES (?, ?, ?)", (1, 2, 3))

    # Commit changes and close connection
    connection.commit()
    connection.close()

# Create tables
create_tables()

# Insert sample data
insert_sample_data()
