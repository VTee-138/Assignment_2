from bus_route import BusRouteBST
from customer import PassengerList
from booking import BookingList

def main():
    print("\n--- Bus Ticket Management System ---\n")

    # Initialize data structures
    bus_routes = BusRouteBST()
    passengers = PassengerList()
    bookings = BookingList()

    while True:
        print("\nMain Menu:")
        print("1. Bus Routes Management")
        print("2. Passenger List Management")
        print("3. Booking Management")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            manage_bus_routes(bus_routes)
        elif choice == "2":
            manage_passengers(passengers)
        elif choice == "3":
            manage_bookings(bus_routes, passengers, bookings)
        elif choice == "4":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def manage_bus_routes(bus_routes):
    print("\n--- Bus Routes Management ---")
    # Add options for managing bus routes
    # Placeholder for bus route management menu

def manage_passengers(passengers):
    print("\n--- Passenger List Management ---")
    # Add options for managing passengers
    # Placeholder for passenger management menu

def manage_bookings(bus_routes, passengers, bookings):
    print("\n--- Booking Management ---")
    # Add options for managing bookings
    # Placeholder for booking management menu

if __name__ == "__main__":
    main()