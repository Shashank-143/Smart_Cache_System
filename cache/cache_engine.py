from cache.data_structures.node import Node
from cache.policies.lru import LRUCachePolicy
from cache.policies.lfu import LFUCachePolicy
from cache.policies.random_policy import RandomPolicy
from cache.policies.priority_policy import PriorityPolicy
from cache.policies.arc import ARCPolicy
from cache.policies.tinylfu import TinyLFUPolicy


class CacheEngine:

    def __init__(self, capacity, policy):

        self.capacity = capacity
        self.store = {}
        self.evictions = 0
        self.hits = 0
        self.misses = 0

        if policy == "LRU":
            self.policy = LRUCachePolicy()
        elif policy == "LFU":
            self.policy = LFUCachePolicy()
        elif policy == "Random":
            self.policy = RandomPolicy()
        elif policy == "Priority":
            self.policy = PriorityPolicy()
        elif policy == "ARC":
            self.policy = ARCPolicy(capacity)
        elif policy == "TinyLFU":
            self.policy = TinyLFUPolicy()    
        else:
            raise ValueError("Invalid policy")

    def get(self, key):

        if key in self.store:

            node = self.store[key]
            self.policy.record_access(node)

            self.hits += 1
            return node.value

        self.misses += 1
        return None

    def put(self, key, value):

        if key in self.store:

            node = self.store[key]
            node.value = value
            self.policy.record_access(node)
            return

        if len(self.store) >= self.capacity:

            node = self.policy.evict()

            if node and node.key in self.store:
                del self.store[node.key]
                self.evictions += 1

        new_node = Node(key, value)
        self.store[key] = new_node
        self.policy.record_access(new_node)