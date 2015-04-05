a = 2510
while a > 1:
    for b in range(2,11):
        c = a % b
        if c == 1:
            a = a + 1
            break
        if b == 10 and c == 0:
            print("\n\nThe number is", a, "\n\n")
            a=0
            break
        