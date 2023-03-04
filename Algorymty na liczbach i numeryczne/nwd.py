
print("Podaj 1 wartosc: ")
a = int(input())
print("Podaj 2 wartosc: ")
b = int(input())

while(b != 0):
    r = a % b
    a = b
    b = r

print("NWD " + str(a))
