class EvictionPolicy:

    def record_access(self, node):
        raise NotImplementedError

    def evict(self):
        raise NotImplementedError