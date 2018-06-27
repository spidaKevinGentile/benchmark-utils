#!/usr/bin/env python3

# Process random data in an attempt to randomize any cached data
import random
g = []
d = []
for i in range(1, 9999):
    g.append(random.randint(0,i))
    for j in range(len(g)):
        d.append(g[j])
print("done.")