# Sortowanie przez wybieranie polega na postawieniu 'ściany' między posortowaną i nieposortowaną częścią zbioru. W
# kolejnych iteracjach algorytmu porównujemy element spoza posortowanej części zbioru z resztą dopóki nie natkniemy się
# na mniejszą od niej wartość np. 2 < 3 lub 1 < 3. Jego złożoność jest kwadratowa ze względu na ciągłość w formie ciągu
# arytmetycznego co wykazujemy wzorem: (n-1)*(1+n-1)/2=(n^2-n)/2. Złożoność ta reprezentuje ten algorytm w najgorszym
# wypadku.
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
for k in range(1, len(t)):
    for i in range(k-1, -1, -1):
        if t[i+1] < t[i]:
            t[i], t[i+1] = t[i+1], t[i]
        else:
            break
# ----------------------------------------------

print("Posortowane: " + str(t))
