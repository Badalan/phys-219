# !python3
import numpy as np


def variance(N, data, avg):
    sums = 0
    for x in data:
        avgDiff = x - avg
        sums += avgDiff**2
    return (1/(N-1))*sums


def stdev(vary):
    return np.sqrt(vary)

data = [4.64, 4.71]
N = 2
avg = np.mean(data)
vary = variance(N, data, avg)
stdeviation = stdev(vary)
print('Variance', vary)
print('Standard Deviation', stdeviation)
