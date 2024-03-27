import sys
input = sys.stdin.readline

stack = []
result = 0
point = 1
x = list(input())

for i in range(len(x)):
    if x[i] == '(':
        point *= 2
        stack.append(x[i])

    elif x[i] == '[':
        point *= 3
        stack.append(x[i])

    elif x[i] == ')':
        if not stack or stack[-1] != '(':
            result = 0
            break
        if x[i-1] == '(':
            result += point
        point //= 2
        stack.pop()

    elif x[i] == ']':
        if not stack or stack[-1] != '[':
            result = 0
            break
        if x[i-1] == '[':
            result += point
        point //= 3
        stack.pop()

if stack:
    print(0)
else:
    print(result)