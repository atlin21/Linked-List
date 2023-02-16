class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    def insert(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("nothing i")
            return
        x = self.head
        llstr = " "
        while x:
            llstr += str(x.data) + " "
            x = x.next
        print(llstr)

    def insert_end(self, data):
        if self.head is None:
            self.head = Node(data)
            return
        x = self.head
        while x.next:
            x = x.next
        x.next = Node(data)

ll = LinkedList()
ll.insert(10)
ll.insert(30)
ll.insert_end(12)
ll.print()

