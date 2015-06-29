#Largest palindrome product

#Problem 4

#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.

x = 100
while x < 1000:
	b = 0
	z = x * x
	liters = str(z)
	if len(liters) > 5:
		if liters[0] == liters[5] and liters[1] == liters[4] and liters[2] == liters[3]:
			print z
			print x
		
	x +=1
	
