from typing import Optional, Any
from cache.data_structures.node import Node

class DoublyLinkedList:
    """A doubly linked list implementation for caching."""

    def __init__(self) -> None:
        """Initializes an empty DoublyLinkedList."""
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None

    def add_to_front(self, node: Node) -> None:
        """
        Adds a node to the front of the list.

        Args:
            node (Node): The node to add.
        """
        node.prev = None
        node.next = self.head

        if self.head:
            self.head.prev = node

        self.head = node

        if self.tail is None:
            self.tail = node

    def move_to_front(self, node: Node) -> None:
        """
        Moves an existing node to the front of the list.

        Args:
            node (Node): The node to move.
        """
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
        if self.head:
            self.head.prev = node
        self.head = node

    def remove_tail(self) -> Optional[Node]:
        """
        Removes and returns the tail node of the list.

        Returns:
            Optional[Node]: The removed tail node, or None if the list is empty.
        """
        if self.tail is None:
            return None

        node: Node = self.tail

        if node.prev:
            node.prev.next = None

        self.tail = node.prev

        if self.tail is None:
            self.head = None

        return node
