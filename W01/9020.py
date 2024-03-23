def is_prime(num):
    if num == 1:
        return False
    for k in range(2, num):
        if num % k == 0:
            return False
    return True


def gold(a, b):
    if is_prime(a) and is_prime(b):
        print(a, b)
    else:
        a -= 1
        b += 1
        gold(a, b)

T = int(input())

for i in range(T):
    n = int(input())
    gold(n//2, n//2)

