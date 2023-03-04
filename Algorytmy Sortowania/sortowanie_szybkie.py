# Wyznaczamy tak zwanego pivota po czym porównujemy liczby i przestawiamy je ze względu na większość lub mniejszość
# od naszej wyznaczonej wartości. Na końcu każdej pętli ustawiamy pivot w jego docelowym miejscu i ten sam algorytm
# wykonujemy na kolejnych częściach po lewo i prawo od pivota aż dojdziemy do posorotwanego zbioru. Złożoność tego
# algorytmu jest logarytmiczna w dobrych warunkach a w pesymistycznym przypadku kwadratowa.
import random


def podziel(tab, start, end):
    pivot = tab[end]
    low = start
    high = end - 1

    while True:
        while low <= high and tab[low] <= pivot:
            low += 1
        while low <= high and tab[high] >= pivot:
            high -= 1

        if low <= high:
            tab[low], tab[high] = tab[high], tab[low]
        else:
            break

    tab[end], tab[low] = tab[low], tab[end]
    return low

def quickSort(tab, start, end):
    if start < end:
        pivot = podziel(tab, start, end)
        quickSort(tab, start, pivot-1)
        quickSort(tab, pivot+1, end)
    return tab


print("Podaj wielkość zbioru:")
n = int(input())
t = [0] * n
# wypełniamy tabelę wartościami do posortowania
for i in range(n):
    t[i] = random.randint(0, 100)
print("Nie posortowane:" + str(t))

print("Posortowane: " + str(quickSort(t, 0, len(t)-1)))
