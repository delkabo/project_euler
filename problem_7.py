#10001st prime
#Problem 7

#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

#What is the 10 001st prime number?

prime_n = int(input("Enter the number: "))

def prime_number(num):
	c = 0
	for x in range(1, num+1):
		if num % x == 0:
			c+=1
			
	if c == 2:
		return True
	else:
		return False	
		
def checking():
	simple_n = 0
	step = 1
	while step <= prime_n:
		
		simple_n += 1
				
		if prime_number(simple_n) == True:
			print "Step # " + str(step)
			print "prime number: " + str(simple_n)
			
			step += 1 
			
			if step > 10000000:
				break
		
		
			
checking()							

#for number 10001 prime number = 104743
