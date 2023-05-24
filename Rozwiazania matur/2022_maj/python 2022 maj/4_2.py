import math

def IsPrime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    x = 2
    while x * x <= n:
        if n % x == 0:
            return False
        x = x + 1
    return True

def Czyn(n):
    czynniki = []
    licznik = 0
    dzielnik = 2
    while n > 1:
        if n % dzielnik == 0:
            czynniki.append(dzielnik)
            n = int(n / dzielnik)
            licznik += 1
        else:
            for x in range(n+1):
                if IsPrime(x):
                    if n % x == 0:
                        dzielnik = x
    czynniki.insert(0, licznik)
    return czynniki


file = open('liczby.txt', 'r')
data = []
wynik = []

for line in file:
    data.append(int(line.rstrip()))

for i in range(len(data)):
    wynik.append(Czyn(data[i]))

max_czyn = 0
max_licz = 0

for i in range(len(wynik)):
    if wynik[i][0] > max_czyn:
        max_czyn = wynik[i][0]
        max_licz = data[i]

print(wynik)
print(max_licz, max_czyn)