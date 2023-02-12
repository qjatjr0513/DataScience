count = 11
n1, n2 = 0, 1
x = 0

while x < count:
    if n1 > 0:
        print(n1)
    sum = n1 + n2

    n1 = n2
    n2 = sum

    x += 1
