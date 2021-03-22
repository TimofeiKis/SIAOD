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

aboba=gen()

start = time.time()
z9bl=aboba.sort
print("Время работы : ",(time.time()-start))
