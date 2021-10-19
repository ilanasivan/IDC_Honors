def gcdExtended(a, b):
    if a == 0:
        return b, 0, 1

    gcd,m,n = gcdExtended(b%a, a)

    x = n - (b//a) * m
    y = m

    return gcd,x,y