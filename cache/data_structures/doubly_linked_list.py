
class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_front(self, node):
        node.prev = None
        node.next = self.head

        if self.head:
            self.head.prev = node

        self.head = node

        if self.tail is None:
            self.tail = node

    def move_to_front(self, node):

        if node == self.head:
            return

        if node.prev:
            node.prev.next = node.next

        if node.next:
            node.next.prev = node.prev

        if node == self.tail:
            self.tail = node.prev

        node.prev = None
        node.next = self.head
        self.head.prev = node
        self.head = node

    def remove_tail(self):

        if self.tail is None:
            return None

        node = self.tail

        if node.prev:
            node.prev.next = None

        self.tail = node.prev

        if self.tail is None:
            self.head = None

        return node
