class PassengerNode:
    def __init__(self, passenger_id, passenger_name, phone):
        self.passenger_id = passenger_id
        self.passenger_name = passenger_name
        self.phone = phone
        self.next = None

class PassengerList:
    def __init__(self):
        self.head = None

    def search(self, passenger_id):
        current = self.head
        while current is not None:
            if current.passenger_id == passenger_id:
                return current
            current = current.next
        return None

    def insert(self, passenger_id, passenger_name, phone):
        new_node = PassengerNode(passenger_id, passenger_name, phone)
        
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def input_passenger(self):
        passenger_id = input("Enter passenger ID: ")
        if self.search(passenger_id) is not None:
            print("Passenger ID already exists")
            return

        passenger_name = input("Enter passenger name: ")
        phone = input("Enter phone: ")

        if not phone.isdigit():
            print("Phone must contain digits only")
            return

        self.insert(passenger_id, passenger_name, phone)
        print("Added successfully")

    def display_all(self):
        if self.head is None:
            return

        current = self.head
        while current is not None:
            print(current.passenger_id, current.passenger_name, current.phone)
            current = current.next

    def delete(self, passenger_id):
        if self.head is None:
            return

        if self.head.passenger_id == passenger_id:
            self.head = self.head.next
            print("Deleted successfully")
            return

        current = self.head
        while current.next is not None:
            if current.next.passenger_id == passenger_id:
                current.next = current.next.next
                print("Deleted successfully")
                return
            current = current.next
            
        print("Passenger not found")

    def load_file(self, filename):
        try:
            file = open(filename, "r")
            for line in file:
                data = line.strip().split(",")
                passenger_id = data[0]
                passenger_name = data[1]
                phone = data[2]
                
                if self.search(passenger_id) is None:
                    self.insert(passenger_id, passenger_name, phone)
                    
            file.close()
            print("Load file successfully")
        except:
            print("Cannot open file")

    def save_to_file(self, filename):
        file = open(filename, "w")
        current = self.head
        while current is not None:
            file.write(current.passenger_id + "," + current.passenger_name + "," + current.phone + "\n")
            current = current.next
            
        file.close()
        print("Saved successfully")