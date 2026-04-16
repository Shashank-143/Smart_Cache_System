# Smart Cache System

A benchmarking framework for evaluating and comparing 6 different cache eviction policies: LRU, LFU, ARC, TinyLFU, Priority, and Random.

## Features

- **6 Eviction Policies**: LRU, LFU, Random, Priority, ARC, TinyLFU
- **Comprehensive Metrics**: Hit rate, miss rate, latency, evictions, memory usage
- **Performance Visualization**: Compare policies with generated graphs
- **Workload Simulation**: Zipf and uniform distribution support
- **Efficient Implementation**: O(1) operations with optimized data structures

## Project Structure

```
Smart_Cache_System/
├── main.py                      # Entry point
├── cache/
│   ├── cache_engine.py
│   ├── data_structures/ (node.py, doubly_linked_list.py)
│   └── policies/ (lru.py, lfu.py, arc.py, tinylfu.py, priority_policy.py, random_policy.py)
├── benchmark/
│   ├── benchmark_runner.py
│   ├── workload_generator.py
│   ├── metrics.py
│   └── plots.py
└── results/                     # Output graphs
```

## Installation

```bash
git clone https://github.com/Shashank-143/Smart_Cache_System.git
cd Smart_Cache_System
pip install -r requirements.txt
```

**Requirements**: Python 3.7+, numpy, matplotlib


## Quick Start

```bash
python main.py
```

Executes all 6 policies on a Zipf-distributed workload, displays metrics, and generates comparison graphs.

## Usage

### Creating a Cache

```python
from cache.cache_engine import CacheEngine

cache = CacheEngine(capacity=100, policy="LRU")
cache.put("key1", "value1")
value = cache.get("key1")
print(f"Hit Rate: {cache.hits / (cache.hits + cache.misses)}")
```

### Available Policies

```python
cache_lru = CacheEngine(100, policy="LRU")         # Least Recently Used
cache_lfu = CacheEngine(100, policy="LFU")         # Least Frequently Used
cache_arc = CacheEngine(100, policy="ARC")         # Adaptive Replacement
cache_tinylfu = CacheEngine(100, policy="TinyLFU") # Lightweight LFU
cache_priority = CacheEngine(100, policy="Priority")
cache_random = CacheEngine(100, policy="Random")
```

### Generating Workloads

```python
from benchmark.workload_generator import WorkloadGenerator

zipf_workload = WorkloadGenerator(distribution="zipf", operations=10000).generate()
uniform_workload = WorkloadGenerator(distribution="uniform", operations=10000).generate()
```

### Running Benchmarks

```python
from cache.cache_engine import CacheEngine
from benchmark.workload_generator import WorkloadGenerator
from benchmark.benchmark_runner import BenchmarkRunner

cache = CacheEngine(100, policy="LRU")
workload = WorkloadGenerator("zipf", operations=20000).generate()
runner = BenchmarkRunner(cache, workload)
results = runner.run()

print(f"Hit Rate: {results['hit_rate']:.4f}")
print(f"Avg Latency: {results['avg_latency']:.8f}")
print(f"Memory Usage: {results['memory_usage']} bytes")
```

## Performance Metrics

| Metric | Description |
|--------|-------------|
| **Hit Rate** | hits / (hits + misses) |
| **Miss Rate** | misses / (hits + misses) |
| **Avg Latency** | average time per operation |
| **Evictions** | number of items removed |
| **Memory Usage** | total bytes consumed |

## Benchmark Output

Running `python main.py` generates:
- Performance comparison table
- Hit/miss rate comparison graphs
- Latency and memory usage charts
- Best-performing policy recommendation

## Policy Recommendations

- **Web Caching**: Use LRU (temporal locality)
- **Database Queries**: Use ARC (adapts to patterns)
- **Long-Running Services**: Use LFU (learns patterns)
- **Priority Data**: Use Priority policy
- **Testing Baseline**: Use Random

## Algorithm Details

| Policy | Time Complexity | Best Use Case |
|--------|-----------------|----------------|
| **LRU** | O(1) | General workloads, temporal locality |
| **LFU** | O(1) avg | Long-term frequency patterns |
| **ARC** | O(1) | Mixed workloads, adaptive systems |
| **TinyLFU** | O(1) | Memory-constrained systems |
| **Priority** | O(log n) | Weighted data importance |
| **Random** | O(1) | Benchmarking baseline |