class RouteNode:
    def __init__(self, route_code, route_name, capacity, available_seats, fare, departure_time):
        self.route_code = route_code
        self.route_name = route_name
        self.capacity = capacity
        self.available_seats = available_seats
        self.fare = fare
        self.departure_time = departure_time
        self.left = None
        self.right = None


class BusRouteBST:
    def __init__(self):
        self.root = None

    def insert(self, node, route_code, route_name, capacity, available_seats, fare, departure_time):
        if node is None:
            return RouteNode(route_code, route_name, capacity, available_seats, fare, departure_time)

        if route_code < node.route_code:
            node.left = self.insert(node.left, route_code, route_name, capacity, available_seats, fare, departure_time)
        elif route_code > node.route_code:
            node.right = self.insert(node.right, route_code, route_name, capacity, available_seats, fare, departure_time)
        else:
            print("Route code already exists")

        return node

    def input_route(self):
        route_code = input("Enter route code: ")
        route_name = input("Enter route name: ")
        capacity = int(input("Enter capacity: "))
        available_seats = int(input("Enter available seats: "))
        fare = float(input("Enter fare: "))
        departure_time = input("Enter departure time: ")
        
        self.root = self.insert(self.root, route_code, route_name, capacity, available_seats, fare, departure_time)
        print("Inserted successfully")

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.route_code, node.route_name, node.capacity, node.available_seats, node.fare, node.departure_time)
            self.inorder(node.right)

    def breadth_first(self):
        if self.root is None:
            return

        queue = []
        queue.append(self.root)

        while len(queue) > 0:
            node = queue.pop(0)
            print(node.route_code, node.route_name, node.capacity, node.available_seats, node.fare, node.departure_time)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    def search(self, node, route_code):
        if node is None or node.route_code == route_code:
            return node

        if route_code < node.route_code:
            return self.search(node.left, route_code)

        return self.search(node.right, route_code)

    def delete_node(self, node, route_code):
        if node is None:
            return node

        if route_code < node.route_code:
            node.left = self.delete_node(node.left, route_code)
        elif route_code > node.route_code:
            node.right = self.delete_node(node.right, route_code)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            min_node = node.right
            while min_node.left is not None:
                min_node = min_node.left

            node.route_code = min_node.route_code
            node.route_name = min_node.route_name
            node.capacity = min_node.capacity
            node.available_seats = min_node.available_seats
            node.fare = min_node.fare
            node.departure_time = min_node.departure_time

            node.right = self.delete_node(node.right, min_node.route_code)

        return node

    def count_nodes(self, node):
        if node is None:
            return 0
        return 1 + self.count_nodes(node.left) + self.count_nodes(node.right)

    def store_inorder(self, node, nodes):
        if node is None:
            return
        self.store_inorder(node.left, nodes)
        nodes.append(node)
        self.store_inorder(node.right, nodes)

    def build_tree(self, nodes, start, end):
        if start > end:
            return None
        mid = (start + end) // 2
        node = nodes[mid]
        node.left = self.build_tree(nodes, start, mid - 1)
        node.right = self.build_tree(nodes, mid + 1, end)
        return node

    def balance(self):
        nodes = []
        self.store_inorder(self.root, nodes)
        self.root = self.build_tree(nodes, 0, len(nodes) - 1)
        print("Balanced successfully")

    def load_file(self, filename):
        try:
            file = open(filename, "r")
            for line in file:
                data = line.strip().split(",")
                route_code = data[0]
                route_name = data[1]
                capacity = int(data[2])
                available_seats = int(data[3])
                fare = float(data[4])
                departure_time = data[5]
                self.root = self.insert(self.root, route_code, route_name, capacity, available_seats, fare, departure_time)
            file.close()
            print("Load file successfully")
        except:
            print("Cannot open file")

    def save_inorder(self, node, file):
        if node:
            self.save_inorder(node.left, file)
            file.write(node.route_code + "," + node.route_name + "," + str(node.capacity) + "," + str(node.available_seats) + "," + str(node.fare) + "," + node.departure_time + "\n")
            self.save_inorder(node.right, file)

    def save_to_file(self, filename):
        file = open(filename, "w")
        self.save_inorder(self.root, file)
        file.close()
        print("Saved successfully")