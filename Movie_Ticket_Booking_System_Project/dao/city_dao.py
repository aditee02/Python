from Model.City import City
from database.connection import DatabaseConnection

class CityDAO:
    def __init__(self, db=None):
        self.db = db or DatabaseConnection.get_connection()
        self.cursor = self.db.cursor()

    def create_city(self, name):
        query = "INSERT INTO city (name) VALUES (%s)"
        self.cursor.execute(query, (name,))
        self.db.commit()
        return self.cursor.lastrowid

    def get_city_by_id(self, city_id):
        query = "SELECT * FROM city WHERE city_id=%s"
        self.cursor.execute(query, (city_id,))
        row = self.cursor.fetchone()
        return City(*row) if row else None

    def get_all_cities(self):
        self.cursor.execute("SELECT * FROM city")
        rows = self.cursor.fetchall()
        return [City(*r) for r in rows]

    def close(self):
        self.cursor.close()
        self.db.close()
