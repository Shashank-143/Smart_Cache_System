
from cache.data_structures.doubly_linked_list import DoublyLinkedList
from cache.policies.eviction_policy import EvictionPolicy


class LRUCachePolicy(EvictionPolicy):

    def __init__(self):
        self.dll = DoublyLinkedList()

    def record_access(self, node):

        if node.prev or node.next or self.dll.head == node:
            self.dll.move_to_front(node)
        else:
            self.dll.add_to_front(node)

    def evict(self):
        return self.dll.remove_tail()
