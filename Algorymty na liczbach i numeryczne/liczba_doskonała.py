n = int(input())
suma = int(1)
i = 2

while i*i <= n:
    if n % i == 0:
        suma += i
        if n/i != i:
            suma += n / i
    i += 1

if n == suma:
    print("Jest doskonała")
else:
    print("Nie")
