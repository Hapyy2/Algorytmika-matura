def IsPrime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    x = 2
    while x * x <= n:
        if n % x == 0:
            return False
        x += 1
    return True

primes = []
for x in range(10001):
    if IsPrime(x):
        primes.append(x)

print(primes)