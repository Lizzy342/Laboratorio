class Sorter:
    """Ordena listas de enteros en forma ascendente (Bubble Sort)."""

    def bubble_sort(self, vet):
        n = len(vet)
        for i in range(n - 1, 0, -1):          # D1: ciclo externo
            for j in range(0, i):              # D2: ciclo interno
                if vet[j] > vet[j + 1]:        # D3: comparación
                    vet[j], vet[j + 1] = vet[j + 1], vet[j]
        return vet
