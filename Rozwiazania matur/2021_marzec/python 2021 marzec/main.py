file = open('galerie.txt', 'r')
data = []

for line in file:
    line = line.strip()
    data.append(line.split(" "))

zad1 = []

for x in range(len(data)):
    zad1.append(data[x][0])

# [print(item, zad1.count(item)) for item in set(zad1)]

zad2 = []

for miasto in data:
    metraz = 0
    lokale = 0
    i = 2
    while i < len(miasto):
        metraz += int(miasto[i]) * int(miasto[i+1])
        if int(miasto[i]) > 0:
            lokale += 1
        i += 2
    zad2.append([miasto[1], metraz, lokale])

print(zad2)

wynik = open('wynik4_2a.txt', 'w')

for miasto in zad2:
    wynik.write(str(miasto[0]))
    wynik.write(" ")
    wynik.write(str(miasto[1]))
    wynik.write(" ")
    wynik.write(str(miasto[2]))
    wynik.write("\n")

wynik.close()

max_metraz = 0
max_metraz_miasto = ""
low_metraz = 999999
low_metraz_miasto = ""

for galeria in zad2:
    if galeria[1] > max_metraz:
        max_metraz = galeria[1]
        max_metraz_miasto = galeria[0]
    if galeria[1] < low_metraz:
        low_metraz = galeria[1]
        low_metraz_miasto = galeria[0]

print(max_metraz_miasto, max_metraz)
print(low_metraz_miasto, low_metraz)

zad4 = []

for miasto in data:
    lokale = []
    i = 2
    while i < len(miasto):
        if int(miasto[i]) > 0:
            lokale.append(int(miasto[i]) * int(miasto[i+1]))
        i += 2
    zad4.append([miasto[1], len(set(lokale))])

max_lokale = 0
max_lokale_miasto = ""
min_lokale = 9999
min_lokale_miasto = ""

for miasto in zad4:
    if miasto[1] > max_lokale:
        max_lokale = miasto[1]
        max_lokale_miasto = miasto[0]
    if miasto[1] < min_lokale:
        min_lokale = miasto[1]
        min_lokale_miasto = miasto[0]

print(max_lokale_miasto, max_lokale)
print(min_lokale_miasto, min_lokale)