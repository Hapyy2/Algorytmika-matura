#Algorytm szybkiego potegowania

print("Podaj liczbe potęgowaną: ")
a = int(input())
print("Podaj wykładnik: ")
b = int(input())

w = 1
c = a
while(b > 0):
    bit = b % 2             #przekształcamy wykładnik na binarny
    b = int(b / 2)
    if bit == 1:            #jeśli mamy bit wysoki to przemnażamy o c
        w = w * c
    c = c * c               #cały czas potęgujemy o 2

print("Twój wynik to: " + str(w))
