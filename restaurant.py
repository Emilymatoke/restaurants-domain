class Restaurant:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def reviews(self, cursor):
        cursor.execute("SELECT * FROM reviews WHERE restaurant_id = ?", (self.id,))
        return cursor.fetchall()

    def customers(self, cursor):
        cursor.execute("""
            SELECT DISTINCT customers.first_name, customers.last_name
            FROM customers
            JOIN reviews ON reviews.customer_id = customers.id
            WHERE reviews.restaurant_id = ?
        """, (self.id,))
        return cursor.fetchall()

    @classmethod
    def fanciest(cls, cursor):
        cursor.execute("SELECT * FROM restaurants ORDER BY price DESC LIMIT 1")
        data = cursor.fetchone()
        return cls(*data)

    def all_reviews(self, cursor):
        cursor.execute("""
            SELECT customers.first_name, customers.last_name, reviews.star_rating
            FROM reviews
            JOIN customers ON reviews.customer_id = customers.id
            WHERE reviews.restaurant_id = ?
        """, (self.id,))
        reviews = cursor.fetchall()
        formatted_reviews = [f"Review for {self.name} by {review[0]} {review[1]}: {review[2]} stars." for review in reviews]
        return formatted_reviews
