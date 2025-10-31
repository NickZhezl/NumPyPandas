import numpy as np

a = np.array([np.random.randint(1, 10, 10) for _ in range(5)])
print("Исходный массив:")
print(a)
print()

indices_to_del = []

unique_rows, indices = np.unique(a, axis=0, return_index=True)
result = a[indices]
print('Уникальный массив')
print(result)

