
import numpy as np


m = np.array([[1, 2, 3],
              [2, 3 ,5],
              [3, 3, 3],
              [4, 5, 7],
              [3, 1 ,3],
              [6, 8, 4],
              [5, 5, 5],
              [1, 3, 7],
              [2, 6, 1],
              [9, 1, 3]],
             )
print(f'Old matrix: \n{m}\n')
indices_to_del = []
for i in range(len(m)):
    if m[i][0] == m[i][1] == m[i][2]:
        indices_to_del.append(i)

new_m = np.delete(m, indices_to_del, axis=0)
print(f'New matrix: \n{new_m}')





