def heapify(vetor, n, i):
    maior = i
    esquerda = 2 * i + 1
    direita = 2 * i + 2

    if esquerda < n and vetor[esquerda].gravidade > vetor[maior].gravidade:
        maior = esquerda

    if direita < n and vetor[direita].gravidade > vetor[maior].gravidade:
        maior = direita

    if maior != i:
        vetor[i], vetor[maior] = vetor[maior], vetor[i]
        heapify(vetor, n, maior)


def heap_sort(vetor):
    n = len(vetor)

    for i in range(n // 2 - 1, -1, -1):
        heapify(vetor, n, i)

    for i in range(n - 1, 0, -1):
        vetor[i], vetor[0] = vetor[0], vetor[i]
        heapify(vetor, i, 0)