from Model.User import User
from database.connection import DatabaseConnection

class UserDAO:
    def __init__(self, db=None):
        if db:
            self.db = db
        else:
            self.db = DatabaseConnection.get_connection()
        self.cursor = self.db.cursor()

    def create_user(self, username, name, password, email, phone_no):
        query = """
        INSERT INTO user (username, name, password, email, phone_no)
        VALUES (%s, %s, %s, %s, %s)
        """
        self.cursor.execute(query, (username, name, password, email, phone_no))
        self.db.commit()
        return self.cursor.lastrowid

    def get_user_by_id(self, user_id):
        query = "SELECT * FROM user WHERE user_id=%s"
        self.cursor.execute(query, (user_id,))
        result = self.cursor.fetchone()
        if result:
            return User(*result)
        return None

    def get_user_by_username(self, username):
        query = "SELECT * FROM user WHERE username=%s"
        self.cursor.execute(query, (username,))
        result = self.cursor.fetchone()
        if result:
            return User(*result)
        return None

    def get_all_users(self):
        query = "SELECT * FROM user"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        return [User(*row) for row in rows]

    def close(self):
        self.cursor.close()
        self.db.close()
