import numpy as np

arr = np.random.randint(0, 10, 10)
print(f"Исходный массив {arr}")

max_index = np.argmax(arr)
print(f'Максимальный элемент {arr[max_index]}')
arr[max_index] = 0
print(f'New mass {arr}')

