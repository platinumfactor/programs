def primefactors(x):
    """ prime factors of a number """
    the_factor_list = []
    the_loop = 2
    while the_loop <= x:
        if x % the_loop == 0:
            x /= the_loop
            the_factor_list.append(the_loop)
        else:
            the_loop += 1
    return the_factor_list
# print(primefactors(13195))
print(primefactors(600851475143))
