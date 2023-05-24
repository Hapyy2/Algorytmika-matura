file = open('instrukcje.txt', 'r')
data = []

for line in file:
    line = line.strip()
    data.append(line.split(" "))

print(data)

dlugosc = 0
for x in range(len(data)):
    if data[x][0] == "DOPISZ":
        dlugosc += 1
    elif data[x][0] == "USUN":
        dlugosc -= 1

print(dlugosc)

licznik = 0
instrukcja = str
max_licz = 0
max_ins = str

for x in range(len(data)):
    if data[x][0] == data[x-1][0]:
        licznik += 1
    else:
        licznik = 1
        intrukcja = data[x][0]
    if licznik > max_licz:
        max_licz = licznik
        max_ins = data[x][0]

print(max_ins, max_licz)

alfabet = []
for x in range(26):
    alfabet.append([chr(ord('A') + x), 0])

for x in range(len(data)):
    if data[x][0] == "DOPISZ":
        dopisywana = data[x][1]
        for x in range(26):
            if alfabet[x][0] == dopisywana:
                alfabet[x][1] += 1

max_literka = 0
max_ilosc = 0
for x in range(len(alfabet)):
    if alfabet[x][1] > max_ilosc:
        max_ilosc = alfabet[x][1]
        max_literka = alfabet[x][0]

print(max_literka, max_ilosc)

wynik = []

for x in range(len(data)):
    if data[x][0] == "DOPISZ":
        wynik.append(data[x][1])
    elif data[x][0] == "USUN":
        wynik.pop()
    elif data[x][0] == "ZMIEN":
        wynik[len(wynik)-1] = data[x][1]
    elif data[x][0] == "PRZESUN":
        for i in range(len(wynik)):
            if wynik[i] == data[x][1]:
                if ord(wynik[i]) == 90:
                    wynik[i] = "A"
                else:
                    wynik[i] = chr(ord(wynik[i])+1)
                break

haslo = ""

for x in range(len(wynik)):
    haslo += wynik[x]

print(haslo)