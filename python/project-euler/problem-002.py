a, b, x, d, e = 1, 2, 0, 0, 2
while x<=4000000:
    x = a + b
    if x < 4000000:
        a = b
        b = x
        d = x%2
        if d == 0:
            e += x
print("The sum of evens is", e)