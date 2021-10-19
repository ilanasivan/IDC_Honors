def exponentiation(x,y, N):
	if y == 0:
		return 1

	myValue = exponentiation(x, y/2, N)

	if (y%2 == 0):
		return (myValue*myValue) % N
	else:	
		return (x*(myValue*myValue)) % N