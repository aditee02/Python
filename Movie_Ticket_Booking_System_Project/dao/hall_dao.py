from Model.Hall import Hall
from database.connection import DatabaseConnection

class HallDAO:
    def __init__(self, db=None):
        self.db = db or DatabaseConnection.get_connection()
        self.cursor = self.db.cursor()

    def create_hall(self, cinema_id, hall_number):
        query = "INSERT INTO hall (cinema_id, hall_number) VALUES (%s, %s)"
        self.cursor.execute(query, (cinema_id, hall_number))
        self.db.commit()
        return self.cursor.lastrowid

    def get_hall_by_id(self, hall_id):
        query = "SELECT * FROM hall WHERE hall_id=%s"
        self.cursor.execute(query, (hall_id,))
        result = self.cursor.fetchone()
        return Hall(*result) if result else None

    def get_all_halls(self):
        query = "SELECT * FROM hall"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        return [Hall(*row) for row in rows]

    def get_halls_by_cinema(self, cinema_id):
        query = "SELECT * FROM hall WHERE cinema_id=%s"
        self.cursor.execute(query, (cinema_id,))
        rows = self.cursor.fetchall()
        return [Hall(*row) for row in rows]

    def close(self):
        self.cursor.close()
        self.db.close()
