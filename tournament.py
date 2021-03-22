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



aboba= gen()
print(aboba)
start = time.time()
def heapify(matrix, lenght, index):
        maximum = index
        left = 2 * index
        right = 2 * index + 1
        if left < lenght and matrix[maximum] < matrix[left]:
            maximum = left
        if right < lenght and matrix[maximum] < matrix[right]:
            maximum = right
        if maximum != index:
            matrix[index], matrix[maximum] = matrix[maximum], matrix[index]
            heapify(matrix, lenght, maximum)
        return matrix
def tour_sort(matrix):
    for i in range(len(matrix) // 2, -1, -1):
        heapify(matrix, len(matrix), i)
    for i in range(len(matrix) - 1, -1, -1):
        if matrix[0] > matrix[i]:
            matrix[0], matrix[i] = matrix[i], matrix[0]
            heapify(matrix, i, 0)
    print("Время выполнения ТС: ", (time.time() - start)*1000)
z9bl = tour_sort(aboba)





