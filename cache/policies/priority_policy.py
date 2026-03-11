
import heapq
from cache.policies.eviction_policy import EvictionPolicy


class PriorityPolicy(EvictionPolicy):

    def __init__(self):
        self.heap = []
        self.priority_counter = 0

    def record_access(self, node):

        self.priority_counter += 1
        heapq.heappush(self.heap, (self.priority_counter, node))

    def evict(self):

        if not self.heap:
            return None

        _, node = heapq.heappop(self.heap)
        return node
