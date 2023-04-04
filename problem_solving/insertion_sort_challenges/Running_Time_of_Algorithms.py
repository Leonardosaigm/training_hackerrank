def runningTime(arr):
    c = 0
    for i in range(1, len(arr)):
        marcado = arr[i]
        j = i - 1

        while j >= 0 and marcado < arr[j]:
            c += 1
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = marcado
        
    return c


n = 5
arr = [2, 1, 3, 1, 2]
runningTime(arr)