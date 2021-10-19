
# Why do we need 33 bits? 
# To compensate for overflow, we need n+1 bits 
# for an n bit number

# We have a borrow at the end of 1 in the worst case, and we shift it
# to the left one time, making it appear in the 33 bit position
# the result is the xor of that difference and borrow, which is an extra bit


def addition(a,b):
	mySum = a ^ b 
	carry = a & b

	while carry:
		carry= carry<<1 
		mysum2 = mySum ^ carry
		carry2 = mySum&carry
		carry=carry2
		mySum = mySum2

	return mySum


def substract(a,b): 
	borrow = ~a & b
	diff = a ^ b
	while borrow:
		borrow= borrow<<1 
		diff2 = diff ^ borrow
		borrow2 = diff & borrow
		borrow=borrow2
		diff = diff2

	return diff

def multiplication(a,b):
	prod = 0
	i = 0
	while b:
		if b & 1:
			prod = addition(prod, a<<i)
		i = i + 1
		b = b >> 1
	return prod