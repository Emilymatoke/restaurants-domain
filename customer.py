class Customer:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def reviews(self, cursor):
        cursor.execute("SELECT * FROM reviews WHERE customer_id = ?", (self.id,))
        return cursor.fetchall()

    def restaurants(self, cursor):
        cursor.execute("""
            SELECT DISTINCT restaurants.name
            FROM restaurants
            JOIN reviews ON reviews.restaurant_id = restaurants.id
            WHERE reviews.customer_id = ?
        """, (self.id,))
        return cursor.fetchall()

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def favorite_restaurant(self, cursor):
        cursor.execute("""
            SELECT restaurants.name
            FROM restaurants
            JOIN reviews ON reviews.restaurant_id = restaurants.id
            WHERE reviews.customer_id = ?
            ORDER BY reviews.star_rating DESC
            LIMIT 1
        """, (self.id,))
        data = cursor.fetchone()
        return data[0] if data else None

    def add_review(self, cursor, restaurant, rating):
        cursor.execute("INSERT INTO reviews (restaurant_id, customer_id, star_rating) VALUES (?, ?, ?)", (restaurant.id, self.id, rating))

    def delete_reviews(self, cursor, restaurant):
        cursor.execute("DELETE FROM reviews WHERE restaurant_id = ? AND customer_id = ?", (restaurant.id, self.id))