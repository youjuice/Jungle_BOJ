import sys
input = sys.stdin.readline


def divide(x, y, n):
    color = paper[x][y]

    for i in range(x, x+n):
        for j in range(y, y+n):
            if color != paper[i][j]:
                print("(", end="")
                divide(x, y, n//2)
                divide(x, y + n//2, n//2)
                divide(x + n // 2, y, n // 2)
                divide(x + n//2, y + n//2, n//2)
                print(")", end="")
                return

    print(color, end="")

N = int(input())
paper = [list(map(int, input().strip())) for _ in range(N)]

divide(0, 0, N)
