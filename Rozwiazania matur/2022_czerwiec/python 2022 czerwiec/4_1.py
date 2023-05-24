import math

def IsPrime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    for h in range(2, int(math.ceil(math.sqrt(n)))):
        if n % h == 0:
            return False
    return True

file = open('przyklad.txt', 'r')
data = []
mirror = []

for line in file:
    data.append(int(line.strip()))
    mirror.append(line.strip())

for x in range(len(mirror)):
    n = mirror[x]
    p = len(n)-1
    n = int(n)
    w = 0
    while p >= 0:
        w = int(w + ((n % 10) * 10**(p)))
        n = int(n / 10)
        p = p-1
    mirror[x] = w

zad1 = []
for x in range(len(mirror)):
    if mirror[x] % 17 == 0:
        zad1.append(mirror[x])

print(zad1)

max_roznica = 0
max_liczba = 0

print(data)
print(mirror)

for i in range(len(mirror)):
    roznica = abs(int(data[i]) - int(mirror[i]))
    if roznica > max_roznica:
        max_roznica = roznica
        max_liczba = data[i]

print(max_liczba, max_roznica)

zad3 = []

for i in range(len(mirror)):
    if IsPrime(data[i]):
        if IsPrime(mirror[i]):
            zad3.append(data[i])

print(zad3)

zad4 = []

for x in range(len(data)):
    licznik = 1
    for y in range(len(data)):
        if data[x] == data[y]:
            licznik = licznik + 1
    zad4.append([data[x], licznik])

print(len(zad4))

for i in range(len(zad4)):
    if zad4[i][1] == 2:
        licznik = licznik + 1
print("ilość2 ", licznik)