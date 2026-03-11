from cache.cache_engine import CacheEngine
from benchmark.workload_generator import WorkloadGenerator
from benchmark.benchmark_runner import BenchmarkRunner
from benchmark.plots import Plotter


def run_policy(policy):

    cache = CacheEngine(100, policy)

    workload = WorkloadGenerator("zipf", operations=20000).generate()

    runner = BenchmarkRunner(cache, workload)

    return runner.run()


def print_results(results):

    print("\n================ DETAILED RESULTS ================\n")

    for policy, metrics in results.items():

        print(f"Policy: {policy}")
        print(f"Hits: {metrics['hits']}")
        print(f"Misses: {metrics['misses']}")
        print(f"Evictions: {metrics['evictions']}")
        print(f"Hit Rate: {metrics['hit_rate']:.4f}")
        print(f"Miss Rate: {metrics['miss_rate']:.4f}")
        print(f"Average Latency: {metrics['avg_latency']:.8f}")
        print(f"Memory Usage: {metrics['memory_usage']}")
        print("--------------------------------------------------")


def print_comparison_table(results):

    print("\n================ PERFORMANCE COMPARISON TABLE ================\n")

    print(f"{'Policy':<12}{'Hit Rate':<12}{'Miss Rate':<12}{'Avg Latency':<15}{'Evictions':<12}")

    print("-" * 63)

    for policy, metrics in results.items():

        print(
            f"{policy:<12}"
            f"{metrics['hit_rate']:<12.4f}"
            f"{metrics['miss_rate']:<12.4f}"
            f"{metrics['avg_latency']:<15.8f}"
            f"{metrics['evictions']:<12}"
        )


def find_best_policy(results):

    best_policy = None
    best_hit_rate = -1

    for policy, metrics in results.items():

        if metrics["hit_rate"] > best_hit_rate:
            best_hit_rate = metrics["hit_rate"]
            best_policy = policy

    return best_policy, best_hit_rate


def main():

    policies = ["LRU", "LFU", "Random", "Priority"]

    results = {}

    for policy in policies:

        print("Running:", policy)

        results[policy] = run_policy(policy)

    # Detailed metrics
    print_results(results)

    # Comparison table
    print_comparison_table(results)

    # Best policy
    best_policy, hit_rate = find_best_policy(results)

    print("\n================ BEST POLICY ================")
    print(f"Best Cache Policy: {best_policy}")
    print(f"Best Hit Rate: {hit_rate:.4f}")

    # Graphs
    plotter = Plotter(results)

    plotter.plot_hit_rate()
    plotter.plot_miss_rate()
    plotter.plot_latency()
    plotter.plot_memory_usage()

    print("\nGraphs saved in results folder.")


if __name__ == "__main__":
    main()