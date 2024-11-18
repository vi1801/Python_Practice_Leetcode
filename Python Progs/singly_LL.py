class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def print_list(self):
        node = self.head
        while node:
            print(node.data, end="->")
            node = node.next
        print("None")


l1 = LinkedList()
l1.append(10)
l1.append(20)
l1.append(30)
l1.print_list()