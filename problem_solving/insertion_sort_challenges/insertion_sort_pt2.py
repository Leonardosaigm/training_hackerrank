
import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort2(n, arr):
    for i in range(1, n):
        marcado = arr[i]

        j = i - 1
        while j >= 0 and marcado < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = marcado
        print(*arr)



n = 7
arr = [3, 4, 7, 5, 6, 2, 1]
insertionSort2(n, arr)