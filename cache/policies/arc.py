from collections import deque
from cache.policies.eviction_policy import EvictionPolicy


class ARCPolicy(EvictionPolicy):

    def __init__(self, capacity):

        self.capacity = capacity

        self.t1 = deque()
        self.t2 = deque()

        self.b1 = deque()
        self.b2 = deque()

        self.p = 0

    def record_access(self, node):

        key = node.key

        # check if node already in lists
        for n in list(self.t1):
            if n.key == key:
                self.t1.remove(n)
                self.t2.appendleft(n)
                return

        for n in list(self.t2):
            if n.key == key:
                self.t2.remove(n)
                self.t2.appendleft(n)
                return

        if key in self.b1:

            self.p = min(self.capacity, self.p + 1)

            self._replace()

            self.b1.remove(key)
            self.t2.appendleft(node)
            return

        if key in self.b2:

            self.p = max(0, self.p - 1)

            self._replace()

            self.b2.remove(key)
            self.t2.appendleft(node)
            return

        if len(self.t1) + len(self.b1) == self.capacity:

            if len(self.t1) < self.capacity:

                self.b1.pop()
                self._replace()

            else:

                self.t1.pop()

        elif len(self.t1) + len(self.b1) < self.capacity:

            total = len(self.t1) + len(self.t2) + len(self.b1) + len(self.b2)

            if total >= self.capacity:

                if total == 2 * self.capacity:
                    self.b2.pop()

                self._replace()

        self.t1.appendleft(node)

    def _replace(self):

        if len(self.t1) > 0 and (len(self.t1) > self.p):

            node = self.t1.pop()
            self.b1.appendleft(node.key)

        else:

            node = self.t2.pop()
            self.b2.appendleft(node.key)

    def evict(self):

        if self.t1:
            return self.t1.pop()

        if self.t2:
            return self.t2.pop()

        return None