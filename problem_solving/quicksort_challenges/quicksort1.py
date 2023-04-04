# https://www.hackerrank.com/challenges/quicksort1/problem

def particao(vetor, inicio, final):
    pivo = vetor[final]
    i = inicio - 1

    for j in range(inicio, final):
        if vetor[j] <= pivo:
            i += 1
            vetor[i], vetor[j] = vetor[j], vetor[i]
    vetor[i + 1], vetor[final] = vetor[final], vetor[i + 1]
    return i + 1


def quick_sort2(vetor, inicio, final):
    if inicio < final:
        posicao = particao(vetor, inicio, final)
        # Esquerda
        quick_sort2(vetor, inicio, posicao - 1)
        # Direito
        quick_sort2(vetor, posicao + 1, final)
    return vetor

def quickSort(arr):
    vetor = arr
    return quick_sort2(vetor, 0, len(vetor) - 1)


arr =[4, 5, 3, 7, 2]

quickSort(arr)