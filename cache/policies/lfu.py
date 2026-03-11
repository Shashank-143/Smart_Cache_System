import heapq
from cache.policies.eviction_policy import EvictionPolicy


class LFUCachePolicy(EvictionPolicy):

    def __init__(self):
        self.heap = []
        self.counter = {}
        self.time = 0   # tie breaker

    def record_access(self, node):

        if node.key not in self.counter:
            self.counter[node.key] = 0

        self.counter[node.key] += 1
        self.time += 1

        # (frequency, time, node)
        heapq.heappush(self.heap, (self.counter[node.key], self.time, node))

    def evict(self):

        while self.heap:

            freq, t, node = heapq.heappop(self.heap)

            if self.counter.get(node.key, None) == freq:
                del self.counter[node.key]
                return node

        return None