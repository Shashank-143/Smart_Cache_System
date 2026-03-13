import random
from cache.policies.eviction_policy import EvictionPolicy


class RandomPolicy(EvictionPolicy):

    def __init__(self):
        self.nodes = []

    def record_access(self, node):

        if node not in self.nodes:
            self.nodes.append(node)

    def evict(self):

        if not self.nodes:
            return None

        node = random.choice(self.nodes)
        self.nodes.remove(node)

        return node