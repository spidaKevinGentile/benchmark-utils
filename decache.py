#!/usr/bin/env python3

# Process random data null any cached data prior to the benchmark
import random
g = []
for i in range(1, 999999):
    g.append(random.randint(0,i))
print("done.")