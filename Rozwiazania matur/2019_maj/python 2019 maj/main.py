file = open('przyklad.txt', 'r')
data = []

for line in file:
    data.append(int(line.rstrip()))

potegi = []
x = 1
while x < 100000:
    potegi.append(x)
    x = x*3

licznik = 0
for i in range(len(data)):
    for x in range(len(potegi)):
        if data[i] == potegi[x]:
            licznik += 1

print(licznik)

def Silnia(n):
    wynik = 1
    while n > 0:
        wynik = wynik * n
        n -= 1
    return wynik

def SumaSilniCyfr(n):
    wynik = 0
    while n > 0:
        wynik += Silnia(n % 10)
        n = int(n / 10)
    return wynik

for number in data:
    if SumaSilniCyfr(number) == number:
        print(number)

def NWD(a, b):
    if a < b:
        a, b = b, a
    while b > 0:
        r = a % b
        a = b
        b = r
    return a

poczatek = 0
licznik = 3
nwd = 0

for i in range(len(data)-2):
    if NWD(NWD(data[i], data[i+1]), data[i+2]) > 1:
        licznik += 1
        nwd = NWD(NWD(data[i], data[i+1]), data[i+2])
        if poczatek == 0:
            poczatek = data[i]

print(poczatek, licznik, nwd)