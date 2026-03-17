class BookingNode:
    def __init__(self, booking_id, route_code, passenger_id, seats_booked, booking_time):
        self.booking_id = booking_id
        self.route_code = route_code
        self.passenger_id = passenger_id
        self.seats_booked = seats_booked
        self.booking_time = booking_time
        self.next = None

class BookingList:
    def __init__(self):
        self.head = None

    def insert(self, booking_id, route_code, passenger_id, seats_booked, booking_time):
        new_node = BookingNode(booking_id, route_code, passenger_id, seats_booked, booking_time)
        
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        print("Booking added successfully")

    def display_all(self):
        if self.head is None:
            print("No bookings available")
            return

        current = self.head
        while current is not None:
            print(current.booking_id, current.route_code, current.passenger_id, current.seats_booked, current.booking_time)
            current = current.next

    def sort_bookings(self):
        if self.head is None or self.head.next is None:
            return

        swapped = True
        while swapped:
            swapped = False
            current = self.head
            
            while current.next is not None:
                str1 = current.route_code + current.passenger_id
                str2 = current.next.route_code + current.next.passenger_id
                
                if str1 > str2:
                    current.booking_id, current.next.booking_id = current.next.booking_id, current.booking_id
                    current.route_code, current.next.route_code = current.next.route_code, current.route_code
                    current.passenger_id, current.next.passenger_id = current.next.passenger_id, current.passenger_id
                    current.seats_booked, current.next.seats_booked = current.next.seats_booked, current.seats_booked
                    current.booking_time, current.next.booking_time = current.next.booking_time, current.booking_time
                    swapped = True
                current = current.next
        print("Sorted successfully")

    def delete(self, booking_id):
        if self.head is None:
            return None

        if self.head.booking_id == booking_id:
            deleted_node = self.head
            self.head = self.head.next
            return deleted_node

        current = self.head
        while current.next is not None:
            if current.next.booking_id == booking_id:
                deleted_node = current.next
                current.next = current.next.next
                return deleted_node
            current = current.next
            
        return None