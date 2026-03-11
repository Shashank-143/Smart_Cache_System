import random
import numpy as np


class WorkloadGenerator:

    def __init__(self, workload_type="zipf", operations=10000, key_space=1000):

        self.workload_type = workload_type
        self.operations = operations
        self.key_space = key_space

    def generate(self):

        if self.workload_type == "zipf":
            return self._zipf_workload()

        if self.workload_type == "hotspot":
            return self._hotspot_workload()

        return self._uniform_workload()

    def _uniform_workload(self):

        workload = []

        for _ in range(self.operations):

            key = random.randint(1, self.key_space)

            if random.random() < 0.8:
                workload.append(("get", key))
            else:
                workload.append(("put", key, random.randint(1, 10000)))

        return workload

    def _zipf_workload(self):

        workload = []

        zipf_keys = np.random.zipf(1.5, self.operations)

        for k in zipf_keys:

            key = int(k % self.key_space)

            if random.random() < 0.8:
                workload.append(("get", key))
            else:
                workload.append(("put", key, random.randint(1, 10000)))

        return workload

    def _hotspot_workload(self):

        workload = []

        hot_keys = int(self.key_space * 0.2)

        for _ in range(self.operations):

            if random.random() < 0.8:
                key = random.randint(1, hot_keys)
            else:
                key = random.randint(1, self.key_space)

            if random.random() < 0.8:
                workload.append(("get", key))
            else:
                workload.append(("put", key, random.randint(1, 10000)))

        return workload