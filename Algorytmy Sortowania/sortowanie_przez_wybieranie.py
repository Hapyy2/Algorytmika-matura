# Sortowanie przez wybieranie polega na przechodzeniu przez całą tablicę w poszukiwaniu najmniejszej wartości. Po
# przejściu przez całą tablicę i jej znalezieniu algorytm zamienia miejscami wartość z brzegu nieposortowanych wartości
# z nowo znalezioną najmniejszą. Jego złożoność jest kwadratowa
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
# for k in range(0, n-1):
#     najmniejsza = k
#     for i in range(k, n):
#         if t[i] < t[najmniejsza]:
#             najmniejsza = i
#     t[k], t[najmniejsza] = t[najmniejsza], t[k]
    
for i in range(len(t)):
        mini = i
        for j in range(i+1, len(t)):
            if t[mini] > t[j]:
                mini = j
        t[i], t[mini] = t[mini], t[i]
# ----------------------------------------------

print("Posortowane:" + str(t))
