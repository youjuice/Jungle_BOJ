def solve(x, y, z):
    if y == 0:
        return 1
    elif y % 2 == 0:
        return (solve(x, y//2, z) ** 2) % z
    else:
        return (solve(x, y - 1, z)) * x % z

a, b, c = map(int, input().split())
print(solve(a, b, c))
