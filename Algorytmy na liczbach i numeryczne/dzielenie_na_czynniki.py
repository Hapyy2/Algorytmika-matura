n = int(input())
i = int(2)

while (n > 1) & (n % i == 0):
    print(str(i) + ", ")
    n = n / i
i += 1
while n > 1:
    if n % i == 0:
        n = n / i
        print(str(i) + ", ")
    else:
        i += 2
