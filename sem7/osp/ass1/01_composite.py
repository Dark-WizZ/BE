[a, b] = map(int, input("Enter a and b: ").split())


def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


for i in range(a, b + 1):
    if i != 1 and not isPrime(i):
        print(i)
