import numpy as np


a = np.array([[1, 2, 3, 4],
              [4, 5, 6, 7],
              [1, 3, 5, 7],
              [2, 3, 4, 5],
              [1, 2, 5, 6],
              [3, 4, 8, 9],
              [1, 2, 3, 8],
              [1, 2, 3, 4]
              ])

b = np.array([[1, 2],
              [3, 4]])

print(f'Массив A \n{a}\n')
print(f'Массив B \n{b}\n')

result_indices = []

for i, row_a in enumerate(a):
    contains_all_rows = True
    for row_b in b:
        if not all(elem in row_a for elem in row_b):
            contains_all_rows = False
            break
    if contains_all_rows:
        result_indices.append(i)

print(f'Строки в A, содержащие все элем B: {result_indices}')

if result_indices:
    print('Строки:')
    for idx in result_indices:
        print(f'Строка {idx}: {a[idx]}')
else:
    print('Нет таких строк(')