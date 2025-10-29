import numpy as np
arr = np.random.randint(0, 10, 10)
print('Исходный масс', arr)

mask = (arr >= 3) & (arr < 8)
arr[mask] = -arr[mask]
print('New масс', arr)
