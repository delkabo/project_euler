#Sum square difference
#Problem 6

#The sum of the squares of the first ten natural numbers is,
#12 + 22 + ... + 102 = 385

#The square of the sum of the first ten natural numbers is,
#(1 + 2 + ... + 10)2 = 552 = 3025

#Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.

#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

num = int(input("Take the number: "))

def square_sum():
	b = 0
	for x in range(1, num+1):
		b = b + x
		
	b = b**2
	return b	
	
def sum_square():
	b = 0
	for x in range(1, num+1):
		b = b + x**2
		
	return b
	
answer = square_sum() - sum_square()

print answer	

print square_sum()
print sum_square()		
	
	
