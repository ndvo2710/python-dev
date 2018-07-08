def addnum(start, end):
    sum = 0
    for i in range(start, end):
        sum += i
        # print(sum)
        yield
    return sum


g1 = addnum(1,51)
g2 = addnum(51,101)

next(g1)
next(g2)
for i in range(50):
    try:
        g1.send(1)
    except StopIteration as exc:
        sum1 = exc.value
    try:
        g2.send(1)
    except StopIteration as exc:
        sum2 = exc.value
print(sum1 + sum2)