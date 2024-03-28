import sys
input = sys.stdin.readline


def solve(num):
    global count
    original_num = num

    while True:
        x = num // 10
        y = num % 10
        z = (x + y) % 10

        new_num = 10 * y + z
        count += 1

        if new_num == original_num:
            break
        else:
            num = new_num

    return count

N = int(input())
count = 0

solve(N)
print(count)
