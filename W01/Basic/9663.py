def visit(a):
    for i in range(a):
        if chess[i] == chess[a]:
            return False
        if abs(a - i) == abs(chess[a] - chess[i]):
            return False
    return True


def queens(x):
    global count
    if x == n:
        count += 1
        return
    for i in range(n):
        chess[x] = i
        if visit(x) is True:
            queens(x + 1)


n = int(input())
count = 0
chess = [0] * n

queens(0)
print(count)
