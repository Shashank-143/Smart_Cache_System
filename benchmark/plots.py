import matplotlib.pyplot as plt
import os


class Plotter:

    def __init__(self, results):

        self.results = results

        if not os.path.exists("results"):
            os.makedirs("results")

    def plot_hit_rate(self):

        policies = list(self.results.keys())
        values = [self.results[p]["hit_rate"] for p in policies]

        plt.figure(figsize=(10, 6))
        plt.bar(policies, values)
        for i, v in enumerate(values):
            plt.text(i, v + 0.01, f"{v:.4f}", ha='center', va='bottom')

        plt.title("Cache Hit Rate Comparison")
        plt.xlabel("Cache Policy")
        plt.ylabel("Hit Rate")
        plt.tight_layout()

        plt.savefig("results/hit_rate.png")
        plt.close()

    def plot_miss_rate(self):

        policies = list(self.results.keys())
        values = [self.results[p]["miss_rate"] for p in policies]

        plt.figure(figsize=(10, 6))
        plt.bar(policies, values)
        for i, v in enumerate(values):
            plt.text(i, v + 0.01, f"{v:.4f}", ha='center', va='bottom')
        plt.ylim(0, 0.18)
        plt.title("Cache Miss Rate Comparison")
        plt.xlabel("Cache Policy")
        plt.ylabel("Miss Rate")
        plt.tight_layout()

        plt.savefig("results/miss_rate.png")
        plt.close()

    def plot_latency(self):

        policies = list(self.results.keys())
        values = [self.results[p]["avg_latency"] for p in policies]

        plt.figure(figsize=(10, 6))
        plt.bar(policies, values)
        for i, v in enumerate(values):
            plt.text(i, v + 0.00000001, f"{v:.8f}", ha='center', va='bottom')

        plt.title("Average Latency Comparison")
        plt.xlabel("Cache Policy")
        plt.ylabel("Latency (seconds)")
        plt.tight_layout()

        plt.savefig("results/latency.png")
        plt.close()

    def plot_memory_usage(self):

        policies = list(self.results.keys())
        values = [self.results[p]["memory_usage"] for p in policies]

        plt.figure(figsize=(10, 6))
        plt.bar(policies, values)
        for i, v in enumerate(values):
            plt.text(i, v + 0.01, f"{v:.2f}", ha='center', va='bottom')

        plt.title("Memory Usage (Evictions)")
        plt.xlabel("Cache Policy")
        plt.ylabel("Evictions")
        plt.tight_layout()
        plt.savefig("results/memory_usage.png")
        plt.close()