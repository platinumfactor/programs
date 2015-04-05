c = 0
for x in range(1, 1000):
    a, b = x%3, x%5
    if a == 0:
        c += x
        if b == 0:
            continue
    if b == 0:
        c +=x
print("Ths sum is", c)