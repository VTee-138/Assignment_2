class Booking:
    def __init__(self, route_code, passenger_id, seat):
        self.route_code = route_code
        self.passenger_id = passenger_id
        self.seat = seat
        self.next = None

class BookingList:
    def __init__(self):
        self.head = None

    def add_booking(self, route_code, passenger_id, seat):
        new_node = Booking(route_code, passenger_id, seat)
        if self.head is None:
            self.head = new_node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node

    def display(self):
        cur = self.head
        if cur is None:
            print("No booking data")
            return
        while cur:
            print("Route:", cur.route_code,
                  "| Passenger:", cur.passenger_id,
                  "| Seat:", cur.seat)
            cur = cur.next

    def sort_bookings(self):
        arr = []
        cur = self.head
        while cur:
            arr.append((cur.route_code, cur.passenger_id, cur.seat))
            cur = cur.next
        arr.sort(key=lambda x: (x[0], x[1]))
        self.head = None
        for r, p, s in arr:
            self.add_booking(r, p, s)
        print("Bookings sorted successfully")

    def check_passenger(self, passenger_id):
        cur = self.head
        while cur:
            if cur.passenger_id == passenger_id:
                return True
            cur = cur.next
        return False

    def process_booking(self):
        route = input("Route code: ").strip()
        passenger = input("Passenger id: ").strip()
        seat = input("Seat number: ").strip()
        if route == "" or passenger == "" or seat == "":
            print("Input cannot be empty")
            return
        if self.check_passenger(passenger):
            print("Passenger already booked")
            return
        self.add_booking(route, passenger, seat)
        print("Booking success")

    def cancel_booking(self, passenger_id):
        cur = self.head
        prev = None
        while cur:
            if cur.passenger_id == passenger_id:
                if prev is None:
                    self.head = cur.next
                else:
                    prev.next = cur.next
                print("Booking cancelled")
                return
            prev = cur
            cur = cur.next
        print("Booking not found")

    def history(self, passenger_id):
        cur = self.head
        found = False
        while cur:
            if cur.passenger_id == passenger_id:
                print("Route:", cur.route_code,
                      "| Passenger:", cur.passenger_id,
                      "| Seat:", cur.seat)
                found = True
            cur = cur.next
        if not found:
            print("No booking history")

    def revenue(self):
        cur = self.head
        count = 0
        while cur:
            count += 1
            cur = cur.next
        revenue = count * 100
        print("Total bookings:", count)
        print("Total revenue:", revenue)

def pause():
    input("\nPress Enter to continue...")

def booking_list_menu(bl):

    while True:
        print("\n===== BOOKING LIST =====")
        print("1. Input booking")
        print("2. Display bookings")
        print("3. Sort bookings")
        print("0. Back")
        choice = input("Choose: ").strip()

        if not choice.isdigit():
            print("Please enter a number")
            pause()
            continue
        choice = int(choice)

        if choice == 1:
            r = input("Route code: ").strip()
            p = input("Passenger id: ").strip()
            s = input("Seat number: ").strip()

            if r == "" or p == "" or s == "":
                print("Input cannot be empty")
            else:
                bl.add_booking(r, p, s)
            pause()

        elif choice == 2:
            bl.display()
            pause()

        elif choice == 3:
            bl.sort_bookings()
            pause()

        elif choice == 0:
            break
        else:
            print("Invalid choice")
            pause()

def booking_operation_menu(bl):
    while True:
        print("\n===== BOOKING OPERATIONS =====")
        print("1. Process booking")
        print("2. Cancel booking")
        print("3. Passenger booking history")
        print("4. Revenue report")
        print("0. Back")
        choice = input("Choose: ").strip()

        if not choice.isdigit():
            print("Please enter a number")
            pause()
            continue
        choice = int(choice)

        if choice == 1:
            bl.process_booking()
            pause()

        elif choice == 2:
            p = input("Passenger id: ").strip()
            if p == "":
                print("Passenger id cannot be empty")
            else:
                bl.cancel_booking(p)
            pause()

        elif choice == 3:
            p = input("Passenger id: ").strip()
            if p == "":
                print("Passenger id cannot be empty")
            else:
                bl.history(p)
            pause()

        elif choice == 4:
            bl.revenue()
            pause()

        elif choice == 0:
            break

        else:
            print("Invalid choice")
            pause()
