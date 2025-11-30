from Model.Show import Show
from database.connection import DatabaseConnection

class ShowDAO:
    def __init__(self, db=None):
        self.db = db or DatabaseConnection.get_connection()
        self.cursor = self.db.cursor()

    def get_show_by_id(self, show_id):
        query = "SELECT show_id, hall_id, movie_id, show_time FROM movie_show WHERE show_id = %s"
        self.cursor.execute(query, (show_id,))
        res = self.cursor.fetchone()
        if res:
            return Show(*res)
        return None

    def get_all_shows(self):
        query = "SELECT show_id, hall_id, movie_id, show_time FROM movie_show"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        return [Show(*row) for row in rows]

    def get_shows_by_hall(self, hall_id):
        query = "SELECT show_id, hall_id, movie_id, show_time FROM movie_show WHERE hall_id = %s"
        self.cursor.execute(query, (hall_id,))
        rows = self.cursor.fetchall()
        return [Show(*row) for row in rows]

    def close(self):
        self.cursor.close()
        self.db.close()
