Flight Booking Agent App (MakeMyTrip-style)

A simple, fully functional flight booking agent simulation written in pure Python.
Runs in any online Python environment (Chrome-based editors, Repl.it, Google Colab) without any external libraries.

Features

User Management

Create users with name and email

Prevent duplicate email registration

Flight Management

Add flights with airline, flight number, origin, destination, departure/arrival time, price, and seats available

Search flights by origin and destination

Booking & Payment Simulation

Book flights for users

Automatically decrement available seats

Simulates payment success

User Dashboard

View all bookings for a user

Display flight details and booking status

Architecture Overview

Pure Python in-memory data storage using dictionaries for:

users → stores user info

flights → stores flight details

bookings → stores booking info

Simple counters to assign unique IDs to users, flights, and bookings

Functions for creating users, adding/searching flights, booking flights, and displaying dashboards

Runs entirely in single process, no web server needed

Tech Stack

Python 3.x (no external packages)

Uses basic data structures (dict) for storage

Fully synchronous, command-line interface

Folder Structure
flight_booking_app/
│
├─ flight_booking.py       # Main Python script with all logic
└─ README.md              # This documentation
Usage Example
1. Run the app
python flight_booking.py
2. Sample Flow
Create Users
uid1 = create_user("Alice", "alice@example.com")
uid2 = create_user("Bob", "bob@example.com")
Add Flights
fid1 = add_flight("AirPython", "PY101", "DEL", "BOM", "10:00", "12:30", 5000, 5)
fid2 = add_flight("AirPython", "PY102", "DEL", "BLR", "11:00", "13:30", 4000, 2)
Search Flights
results = search_flights("DEL", "BOM")
for fid, f in results:
    print(f"Flight ID: {fid}, Flight Number: {f['flight_number']}, Seats: {f['seats_available']}, Price: {f['price']}")
Book Flights
book_flight(uid1, fid1)
book_flight(uid2, fid1)
View User Dashboard
user_dashboard(uid1)
user_dashboard(uid2)
Example Output
User created! User ID: 1
User created! User ID: 2
Flight added! Flight ID: 1
Flight added! Flight ID: 2

Searching flights from DEL to BOM:
Flight ID: 1, Flight Number: PY101, Seats: 5, Price: 5000

Booking flight for Alice:
Booking confirmed! Booking ID: 1

Booking flight for Bob:
Booking confirmed! Booking ID: 2

Alice's dashboard:
--- Dashboard for Alice ---
Booking ID: 1, Flight: PY101 DEL->BOM, Status: CONFIRMED, Seats left: 4

Bob's dashboard:
--- Dashboard for Bob ---
Booking ID: 2, Flight: PY101 DEL->BOM, Status: CONFIRMED, Seats left: 4




This app does not require FastAPI or any external library.

All data is stored in memory, so exiting the program will reset all users, flights, and bookings.
