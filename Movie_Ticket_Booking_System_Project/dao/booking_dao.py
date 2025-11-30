from Model.Booking import Booking
from database.connection import DatabaseConnection
from datetime import datetime

class BookingDAO:
    def __init__(self, db=None):
        self.db = db or DatabaseConnection.get_connection()
        self.cursor = self.db.cursor()

    def create_booking(self, user_id, show_id, seat_id, price, booking_time=None):
        if booking_time is None:
            booking_time = datetime.now()
        query = """
        INSERT INTO booking (user_id, show_id, seat_id, booking_time, price)
        VALUES (%s, %s, %s, %s, %s)
        """
        self.cursor.execute(query, (user_id, show_id, seat_id, booking_time, price))
        self.db.commit()
        return self.cursor.lastrowid


    def get_booking_by_id(self, booking_id):
        query = "SELECT booking_id, user_id, show_id, seat_id, booking_time, price FROM booking WHERE booking_id=%s"
        self.cursor.execute(query, (booking_id,))
        result = self.cursor.fetchone()
        if result:
            return Booking(*result)
        return None

    def get_bookings_by_user(self, user_id):
        query = "SELECT booking_id, user_id, show_id, seat_id, booking_time, price FROM booking WHERE user_id=%s"
        self.cursor.execute(query, (user_id,))
        rows = self.cursor.fetchall()
        return [Booking(*row) for row in rows]

    def close(self):
        self.cursor.close()
        self.db.close()
