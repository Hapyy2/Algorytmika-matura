# Sortowanie przez scalanie należy do algorytmów, które wykorzystują metodę "dziel i zwyciężaj". Naszą liste dzielimy
# rekurencyjnie aż do momentu powstania pojedynczych zbiorów po czym sortując liniowo scalamy je do siebie. Jest to
# bardzo wydajny algorytm a jego złożoność wynosi n * logn
import random


def mergesort(tab):
    if len(tab) > 1:
        mid = len(tab) // 2
        L = tab[:mid]
        R = tab[mid:]
        mergesort(L)
        mergesort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                tab[k] = L[i]
                i += 1
            else:
                tab[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            tab[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            tab[k] = R[j]
            j += 1
            k += 1
    return tab


print("Podaj wielkość zbioru:")
n = int(input())
t = [0] * n
# wypełniamy tabelę wartościami do posortowania
for i in range(n):
    t[i] = random.randint(0, 100)
print("Nie posortowane:" + str(t))

print("Posortowane: " + str(mergesort(t)))
