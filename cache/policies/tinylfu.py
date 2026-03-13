import heapq
from cache.policies.eviction_policy import EvictionPolicy


class TinyLFUPolicy(EvictionPolicy):

    def __init__(self):

        self.frequency = {}
        self.heap = []
        self.time = 0

    def record_access(self, node):

        key = node.key

        if key not in self.frequency:
            self.frequency[key] = 0

        self.frequency[key] += 1

        self.time += 1

        heapq.heappush(self.heap, (self.frequency[key], self.time, node))

    def evict(self):

        while self.heap:

            freq, t, node = heapq.heappop(self.heap)

            if self.frequency.get(node.key, None) == freq:
                del self.frequency[node.key]
                return node

        return None