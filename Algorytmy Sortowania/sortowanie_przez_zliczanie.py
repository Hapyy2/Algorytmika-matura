# Sortowanie przez zliczanie polega na utworzeniu drugiej tablicy liczników w której zapisywać będziemy ilość wystąpień
# danej liczby w zbiorze. Algorytm ten wymaga znajomośći największej liczby w zbiorze przez co nie jest on uniwersalny.
# Jego złożoność jest liniowa ponieważ przechodzimy przez nas zbiór dwa razy: w celu zliczenia liczników oraz wpisania
# ich w zbiór wyników przez co wychodzi nam to : n * n = 2n - złożoność liniowa
import random

print("Podaj wielkość zbioru:")
n = int(input())
t = [0] * n
licznik = [0] * 101
k = 100  #największa możliwa wartość w algorytmie
# wypełniamy tabelę wartościami do posortowania
for i in range(n):
    t[i] = random.randint(0, 100)
print("Nie posortowane:" + str(t))

# Część kodu odpowiedzialna za algorytm
# ----------------------------------------------
for i in range(n-1, -1, -1):
    licznik[t[i]] += 1

print("Posortowane: ")
for i in range(0, k+1):
    for j in range(0, licznik[i]):
        print(str(i))
# ----------------------------------------------
