# https://www.hackerrank.com/challenges/quicksort2/problem

def Quicksort_2(arr):
    if len(arr) <= 1:
        return arr
    a = arr[0]
    left = []
    right = []
    for i in arr:
        if a > i:
            left.append(i)
        if a < i:
            right.append(i)
    result = Quicksort_2(left) + [a] + Quicksort_2(right)
    print(*result)
    return result

n = int(input())
arr = list(map(int, input().split()))
result = Quicksort_2(arr)