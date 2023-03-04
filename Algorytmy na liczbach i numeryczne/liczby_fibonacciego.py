a = int(1)
b = int(1)
c = int()
n = int(input())

if (n == 1) | (n == 2):
    print("1")

for i in range(3, n+1):
    c = a + b
    a = b
    b = c

print(str(c))
