# Movie Ticket Booking System

A **console-based Python application** for booking movie tickets.  
The system uses **MySQL** as the database and implements the **DAO (Data Access Object) pattern** to interact with tables.

---

## Features

- User registration and management
- Browse cities and cinemas
- View movies and show timings by hall
- Seat selection with availability check
- Booking confirmation with automatic timestamp and price
- Fully relational database with foreign key constraints

---

## Technologies Used

- **Python 3.12.7**
- **MySQL**
- `mysql-connector-python` for database interaction
- Object-Oriented Programming (OOP) for models and DAOs
- Console-based interactive menus

---

## Database Schema

Tables in the system:

- `user` — Stores user details
- `city` — Cities where cinemas are located
- `cinema` — Cinema halls in each city
- `hall` — Halls inside cinemas
- `movie` — Movie details
- `movie_show` — Show timings for each hall
- `seat` — Seats in each hall with types and status
- `booking` — Stores ticket bookings

**Note:** The table `movie_show` is used instead of `show` to avoid SQL reserved keyword conflicts.

---

## ER Diagram

The project includes an **Entity-Relationship (ER) Diagram** to visualize the database schema and table relationships.

## Installation

1. **Clone the repository**

```bash
git clone https://github.com/your-username/movie-ticket-booking-system.git
cd movie-ticket-booking-system
