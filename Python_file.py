# -----------------------------------------
# Flight Booking Agent App (Auto Demo Mode)
# Pure Python - Single File
# -----------------------------------------

# In-memory storage
users = {}
flights = {}
bookings = {}

# ID counters
user_id_counter = 1
flight_id_counter = 1
booking_id_counter = 1


# -------------------------
# USER MANAGEMENT
# -------------------------

def create_user(name, email):
    global user_id_counter

    for u in users.values():
        if u["email"] == email:
            print("Error: Email already registered.")
            return None

    uid = user_id_counter

    users[uid] = {
        "name": name,
        "email": email
    }

    user_id_counter += 1

    print(f"User created! User ID: {uid}")
    return uid


# -------------------------
# FLIGHT MANAGEMENT
# -------------------------

def add_flight(airline, flight_number, origin, destination, departure, arrival, price, seats):
    global flight_id_counter

    fid = flight_id_counter

    flights[fid] = {
        "airline": airline,
        "flight_number": flight_number,
        "origin": origin,
        "destination": destination,
        "departure": departure,
        "arrival": arrival,
        "price": price,
        "seats_available": seats
    }

    flight_id_counter += 1

    print(f"Flight added! Flight ID: {fid}")
    return fid


def search_flights(origin, destination):

    results = []

    for fid, f in flights.items():
        if f["origin"] == origin and f["destination"] == destination:
            results.append((fid, f))

    return results


# -------------------------
# BOOKING SYSTEM
# -------------------------

def book_flight(user_id, flight_id):
    global booking_id_counter

    if user_id not in users:
        print("Invalid user ID")
        return

    if flight_id not in flights:
        print("Invalid flight ID")
        return

    flight = flights[flight_id]

    if flight["seats_available"] <= 0:
        print("No seats available!")
        return

    print("Processing payment... SUCCESS")

    booking_id = booking_id_counter

    bookings[booking_id] = {
        "user_id": user_id,
        "flight_id": flight_id,
        "status": "CONFIRMED"
    }

    booking_id_counter += 1

    flight["seats_available"] -= 1

    print(f"Booking confirmed! Booking ID: {booking_id}")


# -------------------------
# USER DASHBOARD
# -------------------------

def user_dashboard(user_id):

    if user_id not in users:
        print("Invalid user")
        return

    user = users[user_id]

    print("\n-----------------------------")
    print(f"Dashboard for {user['name']}")
    print("-----------------------------")

    found = False

    for bid, b in bookings.items():

        if b["user_id"] == user_id:

            found = True

            flight = flights[b["flight_id"]]

            print(
                f"Booking ID: {bid} | "
                f"Flight: {flight['flight_number']} "
                f"{flight['origin']} -> {flight['destination']} | "
                f"Status: {b['status']} | "
                f"Seats left: {flight['seats_available']}"
            )

    if not found:
        print("No bookings found.")


# -------------------------
# DEMO FLOW (NO INPUT)
# -------------------------

def run_demo():

    print("\n===== Flight Booking Demo =====\n")

    # Create users
    uid1 = create_user("Alice", "alice@example.com")
    uid2 = create_user("Bob", "bob@example.com")

    # Add flights
    fid1 = add_flight("AirPython", "PY101", "DEL", "BOM", "10:00", "12:30", 5000, 5)
    fid2 = add_flight("AirPython", "PY102", "DEL", "BLR", "11:00", "13:30", 4000, 2)

    # Search flights
    print("\nSearching flights from DEL to BOM...\n")

    results = search_flights("DEL", "BOM")

    for fid, f in results:
        print(
            f"Flight ID: {fid} | "
            f"{f['airline']} {f['flight_number']} | "
            f"{f['origin']} -> {f['destination']} | "
            f"Seats: {f['seats_available']} | "
            f"Price: {f['price']}"
        )

    # Book flights
    print("\nBooking flight for Alice\n")
    book_flight(uid1, fid1)

    print("\nBooking flight for Bob\n")
    book_flight(uid2, fid1)

    # Show dashboards
    user_dashboard(uid1)
    user_dashboard(uid2)


# -------------------------
# RUN PROGRAM
# -------------------------

if __name__ == "__main__":
    run_demo()
