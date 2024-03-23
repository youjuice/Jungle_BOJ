def is_prime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

N = int(input())

values = map(int, input().split())
prime_count = 0

for value in values:
    if is_prime(value):
        prime_count += 1

print(prime_count)
