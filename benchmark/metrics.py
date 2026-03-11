class Metrics:

    @staticmethod
    def calculate(hit, miss, evictions, total_time, operations):

        hit_rate = hit / operations
        miss_rate = miss / operations

        if operations > 0:
            avg_latency = total_time / operations
        else:
            avg_latency = 0

        memory_usage = evictions

        return {
            "hit_rate": hit_rate,
            "miss_rate": miss_rate,
            "avg_latency": avg_latency,
            "memory_usage": memory_usage,
            "hits": hit,
            "misses": miss,
            "evictions": evictions
        }