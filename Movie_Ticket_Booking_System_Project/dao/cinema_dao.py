from Model.Cinema import Cinema
from database.connection import DatabaseConnection

class CinemaDAO:
    def __init__(self, db=None):
        self.db = db or DatabaseConnection.get_connection()
        self.cursor = self.db.cursor()

    def create_cinema(self, name, city_id):
        query = """
        INSERT INTO cinema (name, city_id)
        VALUES (%s, %s)
        """
        self.cursor.execute(query, (name, city_id))
        self.db.commit()
        return self.cursor.lastrowid

    def get_cinema_by_id(self, cinema_id):
        query = "SELECT * FROM cinema WHERE cinema_id = %s"
        self.cursor.execute(query, (cinema_id,))
        result = self.cursor.fetchone()
        if result:
            return Cinema(*result)
        return None

    def get_all_cinemas(self):
        query = "SELECT * FROM cinema"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        return [Cinema(*row) for row in rows]

    def get_cinemas_by_city(self, city_id):
        query = "SELECT * FROM cinema WHERE city_id = %s"
        self.cursor.execute(query, (city_id,))
        rows = self.cursor.fetchall()
        return [Cinema(*row) for row in rows]

    def close(self):
        self.cursor.close()
        self.db.close()
