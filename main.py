import sqlite3
from restaurant import Restaurant
from customer import Customer
from review import Review
from database import create_tables, insert_sample_data

# Connect to the database
connection = sqlite3.connect("restaurant_reviews.db")
cursor = connection.cursor()

# Create tables
create_tables(cursor)

# Insert sample data
insert_sample_data(cursor)

# Test your methods here
# For example:
restaurant_a = Restaurant("Restaurant A", 3)
print("Reviews for Restaurant A:", restaurant_a.reviews(cursor))

customer_john = Customer("John", "Doe")
print("Reviews by John:", customer_john.reviews(cursor))

review = Review(restaurant_a, customer_john, 5)
print("Full Review:", review.full_review())

# Don't forget to commit the changes and close the connection
connection.commit()
connection.close()
