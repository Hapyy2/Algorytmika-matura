import math

def IsSame(n):
    pierwsza = int(n[0])
    n = int(n)
    ostatnia = n % 10
    if pierwsza == ostatnia:
        return True
    else:
        return False

file = open('liczby.txt', 'r')
data = []

for line in file:
    data.append(line.rstrip())

licznik = 0
pierwsza = None

for i in range(len(data)):
    if IsSame(data[i]):
        licznik += 1
        if pierwsza is None:
            pierwsza = data[i]

print(licznik, pierwsza)