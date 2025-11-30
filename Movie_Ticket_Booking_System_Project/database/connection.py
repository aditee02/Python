import mysql.connector

class DatabaseConnection:
    @staticmethod
    def get_connection():
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="MOVIE_TICKET_BOOKING_SYSTEM"
        )
