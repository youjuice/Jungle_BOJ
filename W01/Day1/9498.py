def score(x):
    if 90 <= x <= 100:
        return 'A'
    elif 80 <= x < 90:
        return 'B'
    elif 70 <= x < 80:
        return 'C'
    elif 60 <= x < 70:
        return 'D'
    else:
        return 'F'

a = int(input())
print(score(a))