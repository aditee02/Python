from database.connection import DatabaseConnection
import datetime

from dao.user_dao import UserDAO
from dao.city_dao import CityDAO
from dao.cinema_dao import CinemaDAO
from dao.hall_dao import HallDAO
from dao.movie_dao import MovieDAO
from dao.show_dao import ShowDAO
from dao.seat_dao import SeatDAO
from dao.booking_dao import BookingDAO


from Model.Booking import Booking

def get_db():
    return DatabaseConnection.get_connection()

def register(user_dao):
    print("\n--- Register User ---")
    username = input("Username: ")
    name = input("Full Name: ")
    password = input("Password: ")
    email = input("Email: ")
    phone = input("Phone Number: ")

    user_dao.create_user(username, name, password, email, phone)
    print("User registered successfully!")

def login(user_dao):
    print("\n--- Login ---")
    username = input("Username: ")
    password = input("Password: ")

    user = user_dao.get_user_by_username(username)
    if user and user.password == password:
        print(f"\nWelcome {user.name}!")
        return user
    else:
        print("Invalid credentials!")
        return None
    
def choose_city(city_dao):
    cities = city_dao.get_all_cities()
    print("\n--- Select City ---")
    for c in cities:
        print(f"{c.city_id}. {c.name}")
    return int(input("Enter City ID: "))

def choose_cinema(cinema_dao, city_id):
    cinemas = cinema_dao.get_cinemas_by_city(city_id)
    print("\n--- Select Cinema ---")
    for c in cinemas:
        print(f"{c.cinema_id}. {c.name}")
    return int(input("Enter Cinema ID: "))

def choose_hall(hall_dao, cinema_id):
    halls = hall_dao.get_halls_by_cinema(cinema_id)
    print("\n--- Select Hall ---")
    for h in halls:
        print(f"{h.hall_id}. Hall {h.hall_number}")
    return int(input("Enter Hall ID: "))

def choose_movie(movie_dao):
    movies = movie_dao.get_all_movies()
    print("\n--- Select Movie ---")
    for m in movies:
        print(f"{m.movie_id}. {m.title}")
    return int(input("Enter Movie ID: "))

def choose_show(show_dao, hall_id):
    shows = show_dao.get_shows_by_hall(hall_id)
    print("\n--- Select Show ---")
    for s in shows:
        print(f"{s.show_id}. {s.show_time}")
    return int(input("Enter Show ID: "))

def choose_seat(seat_dao, hall_id):
    seats = seat_dao.get_seats_by_hall(hall_id)
    print("\n--- Select Seat ---")
    for s in seats:
        if s.status == "Available":
            print(f"{s.seat_id}. {s.seat_number} ({s.seat_type})")
    return int(input("Enter Seat ID: "))


def confirm_booking(booking_dao, user, show_id, seat_id):
    price = 250.00
    booking_time = str(datetime.datetime.now())

    booking = Booking(
        None, user.user_id, show_id, seat_id, booking_time, price
    )
    booking_dao.create_booking(
        user.user_id, show_id, seat_id, booking_time, price
    )

    print("\n🎉 Ticket Booked Successfully!")
    print(f"Booking Time: {booking_time}")
    print(f"Price: ₹{price}")


def main():
    db = get_db()

    user_dao    = UserDAO(db)
    city_dao    = CityDAO(db)
    cinema_dao  = CinemaDAO(db)
    hall_dao    = HallDAO(db)
    movie_dao   = MovieDAO(db)
    show_dao    = ShowDAO(db)
    seat_dao    = SeatDAO(db)
    booking_dao = BookingDAO(db)

    print("=== MOVIE TICKET BOOKING SYSTEM ===")

    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Choose: ")

        if choice == "1":
            register(user_dao)

        elif choice == "2":
            user = login(user_dao)
            if user:
                city_id   = choose_city(city_dao)
                cinema_id = choose_cinema(cinema_dao, city_id)
                hall_id   = choose_hall(hall_dao, cinema_id)
                movie_id  = choose_movie(movie_dao)
                show_id   = choose_show(show_dao, hall_id)
                seat_id   = choose_seat(seat_dao, hall_id)

                confirm_booking(booking_dao, user, show_id, seat_id)

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice!")

    db.close()


if __name__ == "__main__":
    main()
