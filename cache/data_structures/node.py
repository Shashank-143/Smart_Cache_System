from typing import Optional, Any

class Node:
    """Represents a node in a doubly linked list."""

    def __init__(self, key: Any, value: Any) -> None:
        """
        Initializes a new node.

        Args:
            key (Any): The key stored in the node.
            value (Any): The value stored in the node.
        """
        self.key: Any = key
        self.value: Any = value
        self.prev: Optional['Node'] = None
        self.next: Optional['Node'] = None
