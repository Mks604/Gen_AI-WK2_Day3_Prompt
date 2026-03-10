✈️ Flight Booking Agent App (MakeMyTrip-Style)

A simple flight booking agent simulation written in pure Python.

The application allows users to register, search flights, book seats, and view their booking dashboard — similar to platforms like MakeMyTrip or Skyscanner.

It runs in any Python environment (Replit, Google Colab, VS Code, terminal) without external libraries.

🚀 Features
👤 User Management

Create users with name and email

Prevent duplicate email registration

Assign unique user IDs

✈️ Flight Management

Add flights with details including:

Airline

Flight Number

Origin

Destination

Departure Time

Arrival Time

Ticket Price

Available Seats

Users can search flights by origin and destination.

💳 Booking & Payment Simulation

Book flights for registered users

Automatically reduce seat availability

Simulates successful payment

Generates unique booking ID

📊 User Dashboard

Users can view:

All their bookings

Flight details

Booking status

Remaining seats

🏗 Architecture Overview

The application uses in-memory data structures:

Storage	Purpose
users	Stores user details
flights	Stores flight information
bookings	Stores booking records
ID Generation

Simple counters generate unique IDs:

user_id_counter

flight_id_counter

booking_id_counter

🧰 Tech Stack

Python 3.x

No external libraries

Uses built-in dictionary data structures

Fully synchronous CLI application

📁 Project Structure
flight_booking_app/
│
├── flight_booking.py     # Main application logic
└── README.md             # Project documentation
▶️ How to Run
python flight_booking.py

Works in:

Terminal

VS Code

Replit

Google Colab

Any Python environment
