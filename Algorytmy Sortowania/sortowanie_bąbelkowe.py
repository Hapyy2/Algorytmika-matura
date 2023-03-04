# Sortowanie bąbelkowe tabeli polega na naprzemiennym zamienianu miejscami 2 wartości od lewej do prawej w przypadku
# większości lub mniejszości. Jest to mało wydajny typ sortowania, ponieważ nawet w wypadku braku potrzeby zamiany
# algorytm i tak przez to przechodzi. Jego złożoność jest kwadratowa ze względu na ciągłość w formie ciągu
# arytmetycznego co wykazujemy wzorem: (n-1)*(1+n-1)/2=(n^2-n)/2
import random

print("Podaj wielkość zbioru:")
n = int(input())
t = [0] * n
# wypełniamy tabelę wartościami do posortowania
for i in range(n):
    t[i] = random.randint(0, 100)
print("Nie posortowane:" + str(t))

# Część kodu odpowiedzialna za algorytm
# ----------------------------------------------
for i in range(len(t)):
    for j in range(len(t) - i - 1):
        if t[j] > t[j + 1]:
            t[j + 1], t[j] = t[j], t[j + 1]
# ----------------------------------------------

print("Posortowane:" + str(t))
