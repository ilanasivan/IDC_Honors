from math import ceil, floor

# this program assumes we receive positive numbers
def karatsuba(x, y):

    # base case if numbers are single digit
    if (len(str(x)) ==1 and len(str(y)) ==1):
        return x * y
    
    n = ceil(max(len(str(x)), len(str(y)))//2)

    # store variable to reuse
    m = (10*n)

    a = floor(x // m)
    b = y % m
    c = floor(y // m)
    d = y % m

    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    abcd = karatsuba(a + b, c + d) - ac - bd
    
    # return result
    return int(10 ** (2 * n) * ac + (10 ** n) * abcd + bd)