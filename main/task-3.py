import random

import numpy as np

a = np.array([np.random.randint(1, 10, 10), np.random.randint(1, 10, 10)])
print(f'Первый массив \n{a[0]} \nВторой массив \n{a[1]}')
mult = a[0]*a[1]
print(f'Произведение массивов {mult}')
