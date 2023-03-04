# Założeniem algorytmu jest optymalne obliczenie ilości potrzebnych banknotów do wydania danej sumy (bez monet)

T = [500, 200, 100, 50, 20, 10]
K = [0] * 6
n = int(input())
R = n
i = int(0)

while R > 0:
    K[i] = int(R / T[i])
    R = R % T[i]
    i += 1

print(str(n))
for i in range(len(T)):
    print(str(T[i]) + " x " + str(K[i]))
