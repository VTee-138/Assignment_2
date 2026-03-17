from bus_route import BusRouteBST
from customer import PassengerList
from booking import BookingList

def main():
    bus_routes = BusRouteBST()
    passengers = PassengerList()
    bookings = BookingList()

    while True:
        print("\n1. Bus Routes Management")
        print("2. Passenger List Management")
        print("3. Booking List Management")
        print("4. Route Operations")
        print("5. Booking Operations")
        print("0. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            manage_bus_routes(bus_routes)
        elif choice == "2":
            manage_passengers(passengers)
        elif choice == "3":
            manage_bookings_menu(bookings)
        elif choice == "4":
            manage_route_ops(bus_routes, bookings)
        elif choice == "5":
            manage_booking_ops(bus_routes, passengers, bookings)
        elif choice == "0":
            break
        else:
            print("Invalid choice")

def manage_bus_routes(bus_routes):
    while True:
        print("\n1. Load file")
        print("2. Insert route")
        print("3. In-order")
        print("4. Breadth-first")
        print("5. Save file")
        print("6. Search")
        print("7. Delete by route_code")
        print("8. Balance BST")
        print("9. Count routes")
        print("0. Back")
        
        choice = input("Enter choice: ")
        if choice == "1":
            filename = input("Enter filename: ")
            bus_routes.load_file(filename)
        elif choice == "2":
            bus_routes.input_route()
        elif choice == "3":
            bus_routes.inorder(bus_routes.root)
        elif choice == "4":
            bus_routes.breadth_first()
        elif choice == "5":
            filename = input("Enter filename to save: ")
            bus_routes.save_to_file(filename)
        elif choice == "6":
            code = input("Enter route_code: ")
            node = bus_routes.search(bus_routes.root, code)
            if node:
                print(node.route_code, node.route_name, node.capacity, node.available_seats, node.fare, node.departure_time)
            else:
                print("Not found")
        elif choice == "7":
            code = input("Enter route_code to delete: ")
            bus_routes.root = bus_routes.delete_node(bus_routes.root, code)
            print("Operation completed")
        elif choice == "8":
            bus_routes.balance()
        elif choice == "9":
            count = bus_routes.count_nodes(bus_routes.root)
            print("Total routes:", count)
        elif choice == "0":
            break

def manage_passengers(passengers):
    while True:
        print("\n1. Load file")
        print("2. Insert passenger")
        print("3. Display all")
        print("4. Save file")
        print("5. Search")
        print("6. Delete")
        print("0. Back")
        
        choice = input("Enter choice: ")
        if choice == "1":
            filename = input("Enter filename: ")
            passengers.load_file(filename)
        elif choice == "2":
            passengers.input_passenger()
        elif choice == "3":
            passengers.display_all()
        elif choice == "4":
            filename = input("Enter filename to save: ")
            passengers.save_to_file(filename)
        elif choice == "5":
            p_id = input("Enter passenger_id: ")
            node = passengers.search(p_id)
            if node:
                print(node.passenger_id, node.passenger_name, node.phone)
            else:
                print("Not found")
        elif choice == "6":
            p_id = input("Enter passenger_id to delete: ")
            passengers.delete(p_id)
        elif choice == "0":
            break

def manage_bookings_menu(bookings):
    while True:
        print("\n1. Display all bookings")
        print("2. Sort bookings")
        print("0. Back")
        
        choice = input("Enter choice: ")
        if choice == "1":
            bookings.display_all()
        elif choice == "2":
            bookings.sort_bookings()
        elif choice == "0":
            break

def manage_route_ops(bus_routes, bookings):
    while True:
        print("\n1. Update schedule")
        print("2. Check seats")
        print("3. Most popular routes")
        print("0. Back")
        
        choice = input("Enter choice: ")
        if choice == "1":
            code = input("Enter route_code: ")
            node = bus_routes.search(bus_routes.root, code)
            if node:
                node.departure_time = input("Enter new departure time: ")
                node.fare = float(input("Enter new fare: "))
                node.capacity = int(input("Enter new capacity: "))
                print("Updated successfully")
            else:
                print("Route not found")
        elif choice == "2":
            code = input("Enter route_code: ")
            node = bus_routes.search(bus_routes.root, code)
            if node:
                print("Available seats:", node.available_seats)
            else:
                print("Route not found")
        elif choice == "3":
            codes = []
            counts = []
            current = bookings.head
            while current is not None:
                rc = current.route_code
                found = False
                for i in range(len(codes)):
                    if codes[i] == rc:
                        counts[i] += 1
                        found = True
                        break
                if not found:
                    codes.append(rc)
                    counts.append(1)
                current = current.next
                
            for i in range(len(codes)):
                for j in range(i + 1, len(codes)):
                    if counts[i] < counts[j]:
                        counts[i], counts[j] = counts[j], counts[i]
                        codes[i], codes[j] = codes[j], codes[i]
            
            print("Popular Routes:")
            for i in range(len(codes)):
                print(codes[i], "-", counts[i], "bookings")
        elif choice == "0":
            break

def manage_booking_ops(bus_routes, passengers, bookings):
    while True:
        print("\n1. Process new booking")
        print("2. Cancel booking")
        print("3. Booking history")
        print("4. Daily revenue report")
        print("0. Back")
        
        choice = input("Enter choice: ")
        if choice == "1":
            b_id = input("Enter booking ID: ")
            r_code = input("Enter route code: ")
            p_id = input("Enter passenger ID: ")
            seats = int(input("Enter seats booked: "))
            b_time = input("Enter booking time: ")
            
            route_node = bus_routes.search(bus_routes.root, r_code)
            p_node = passengers.search(p_id)
            
            if route_node is None:
                print("Route not found")
            elif p_node is None:
                print("Passenger not found")
            elif seats > route_node.available_seats:
                print("Not enough available seats")
            else:
                route_node.available_seats -= seats
                bookings.insert(b_id, r_code, p_id, seats, b_time)
        elif choice == "2":
            b_id = input("Enter booking ID to cancel: ")
            deleted_node = bookings.delete(b_id)
            if deleted_node:
                route_node = bus_routes.search(bus_routes.root, deleted_node.route_code)
                if route_node:
                    route_node.available_seats += deleted_node.seats_booked
                print("Booking cancelled successfully")
            else:
                print("Booking not found")
        elif choice == "3":
            p_id = input("Enter passenger ID: ")
            current = bookings.head
            found = False
            while current is not None:
                if current.passenger_id == p_id:
                    print(current.booking_id, current.route_code, current.seats_booked, current.booking_time)
                    found = True
                current = current.next
            if not found:
                print("No history found")
        elif choice == "4":
            dates = []
            revs = []
            current = bookings.head
            while current is not None:
                date = current.booking_time.split()[0]
                route_node = bus_routes.search(bus_routes.root, current.route_code)
                if route_node:
                    revenue = current.seats_booked * route_node.fare
                    found = False
                    for i in range(len(dates)):
                        if dates[i] == date:
                            revs[i] += revenue
                            found = True
                            break
                    if not found:
                        dates.append(date)
                        revs.append(revenue)
                current = current.next
                
            print("Daily Revenue:")
            for i in range(len(dates)):
                print(dates[i], ":", revs[i])
        elif choice == "0":
            break

if __name__ == "__main__":
    main()