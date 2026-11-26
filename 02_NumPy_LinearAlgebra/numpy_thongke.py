import numpy as np
from statistics import mode

arr = np.array([2, 4, 4, 4, 6, 8])

print("Mean:", np.mean(arr))
print("Median:", np.median(arr))
print("Mode:", mode(arr))
print("Variance:", np.var(arr))
print("Standard Deviation:", np.std(arr))
