file = open("identyfikator.txt", "r")
data = []

for line in file:
    data.append(line.strip())

print(data)

# ZADANIE 4.1
zad1 = []
max_suma = 0

for kod in data:
    suma = int(kod[3]) + int(kod[4]) + int(kod[5]) + int(kod[6]) + int(kod[7]) + int(kod[8])
    if suma > max_suma:
        max_suma = suma
for kod in data:
    suma = int(kod[3]) + int(kod[4]) + int(kod[5]) + int(kod[6]) + int(kod[7]) + int(kod[8])
    if suma == max_suma:
        zad1.append([kod, suma])

plik1 = open("wyniki4_1.txt", "w")
for kod in zad1:
    plik1.write(str(kod[0]))
    plik1.write("\n")
plik1.close()
print(zad1)

# ZADANIE 4.2
def Palindrom(n):
    reversed = n[::-1]
    if n == reversed:
        return True
    else:
        return False

zad2= []
for kod in data:
    litery = kod[:3]
    cyfry = kod[3:]
    if Palindrom(litery):
        zad2.append(kod)
    if Palindrom(cyfry):
        zad2.append(kod)

plik2 = open("wyniki4_2.txt", "w")
for kod in zad2:
    plik2.write(str(kod))
    plik2.write("\n")
plik2.close()
print(zad2)

# ZADANIE 4.3
zad3 = []

for kod in data:
    litery = kod[:3]
    kontrolka = int(kod[3])
    cyfry = kod[4:]
    suma = (ord(litery[0])-55) * 7 + (ord(litery[1])-55) * 3 + (ord(litery[2])-55)
    suma += int(cyfry[0]) * 7 + int(cyfry[1]) * 3 + int(cyfry[2]) + int(cyfry[3]) * 7 + int(cyfry[4]) * 3
    suma_kontrolna = suma % 10
    if kontrolka != suma_kontrolna:
        zad3.append(kod)

plik3 = open("wyniki4_3.txt", "w")
for kod in zad3:
    plik3.write(str(kod))
    plik3.write("\n")
plik3.close()
print(zad3)