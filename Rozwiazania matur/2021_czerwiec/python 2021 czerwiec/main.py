file = open('napisy.txt', 'r')
data = []

for line in file:
    data.append(line.strip())

print(data)

licznik_cyfr = 0

for x in range(len(data)):
    for i in range(len(data[x])):
        if ord(data[x][i]) < 65:
            licznik_cyfr += 1

print(licznik_cyfr)

haslo = ""
row = 19
column = 0

while row < 1000:
    haslo += data[row][column]
    row += 20
    column += 1

print(haslo)

zad3 = ""

for line in data:
    op1 = line + line[0]
    op2 = line[len(line) - 1] + line
    if op1 == op1[::-1]:
        zad3 += op1[25]
    elif op2 == op2[::-1]:
        zad3 += op2[25]

print(zad3)

zad4 = ""

for line in data:
    pary = []
    for x in range(len(line)):
        if ord(line[x]) < 65:
            pary.append(line[x])
    if len(pary) % 2 != 0:
        pary.pop()
    i = 0
    while i < len(pary):
        liczba = int(pary[i] + pary[i+1])
        if liczba >= 65 and liczba <= 90:
            zad4 += chr(liczba)
        i += 2

for x in range(1, len(zad4)):
    if zad4[x-1] == "X" and zad4[x] == "X" and zad4[x+1] == "X":
        zad4 = zad4[:x+1]
        break

print(zad4)