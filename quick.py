import random
import time
import numpy as np

def gen(x = 1000, y = 1000, min = -1000, max = 1000):
    matrix = []
    for i in range(x):
        matrix.append([])
        for j in range(y):
            matrix[i].append(random.randint(min, max))
    return matrix

ded=gen()
print(ded)
start = time.time()
def quick_sort(matrix):
    if len(matrix) <= 1:
        return matrix
    prop = matrix[0]
    left = [i for i in matrix if i < prop]
    center = [i for i in matrix if i == prop]
    right = [i for i in matrix if i > prop]
    final_matrix = quick_sort(left) + center + quick_sort(right)
    return final_matrix
finish = time.time()
print("Время работы БС: ",finish-start)
s9el= quick_sort(ded)