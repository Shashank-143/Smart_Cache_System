import time
from benchmark.metrics import Metrics


class BenchmarkRunner:

    def __init__(self, cache, workload):

        self.cache = cache
        self.workload = workload

    def run(self):

        start_time = time.time()

        operations = len(self.workload)

        for operation in self.workload:

            if operation[0] == "get":

                self.cache.get(operation[1])

            elif operation[0] == "put":

                self.cache.put(operation[1], operation[2])

        end_time = time.time()

        total_time = end_time - start_time

        # Collect metrics from cache
        hits = self.cache.hits
        misses = self.cache.misses
        evictions = self.cache.evictions

        results = Metrics.calculate(
            hits,
            misses,
            evictions,
            total_time,
            operations
        )

        return results