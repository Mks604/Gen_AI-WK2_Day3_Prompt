%%writefile flight_booking.py

# Flight Booking Demo
users = {}
flights = {}
bookings = {}

user_id_counter = 1
flight_id_counter = 1
booking_id_counter = 1


def create_user(name, email):
    global user_id_counter
    uid = user_id_counter
    users[uid] = {"name": name, "email": email}
    user_id_counter += 1
    print(f"User created! User ID: {uid}")
    return uid


def add_flight(airline, number, origin, dest, dep, arr, price, seats):
    global flight_id_counter
    fid = flight_id_counter
    flights[fid] = {
        "airline": airline,
        "flight_number": number,
        "origin": origin,
        "destination": dest,
        "departure": dep,
        "arrival": arr,
        "price": price,
        "seats": seats,
    }
    flight_id_counter += 1
    print(f"Flight added! Flight ID: {fid}")
    return fid


def book_flight(uid, fid):
    global booking_id_counter
    if flights[fid]["seats"] <= 0:
        print("No seats available")
        return

    flights[fid]["seats"] -= 1
    bid = booking_id_counter
    bookings[bid] = {"user": uid, "flight": fid}
    booking_id_counter += 1
    print(f"Booking confirmed! Booking ID: {bid}")


def dashboard(uid):
    print("\nUser Dashboard")
    for bid, b in bookings.items():
        if b["user"] == uid:
            f = flights[b["flight"]]
            print(f"Booking {bid}: {f['flight_number']} {f['origin']}->{f['destination']}")


def run_demo():
    uid1 = create_user("Alice", "alice@example.com")
    uid2 = create_user("Bob", "bob@example.com")

    fid1 = add_flight("AirPython", "PY101", "DEL", "BOM", "10:00", "12:30", 5000, 5)

    book_flight(uid1, fid1)
    book_flight(uid2, fid1)

    dashboard(uid1)
    dashboard(uid2)


if __name__ == "__main__":
    run_demo()
