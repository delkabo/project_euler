#Largest prime factor
#Problem 3

#The prime factors of 13195 are 5, 7, 13 and 29.

#What is the largest prime factor of the number 600851475143 ?

print "starting..."

znach = 600851475143
b = 1
z = 0
x = False

while x == False:
	b += 1
	if znach % (znach/b) == 0:
		z = znach/b
		x = True
	print float(znach/b)	
	
	
	
print z	
		
		
print "max multiple: " + str(znach) + " / " +str(z) + " = " + str(znach/(znach/b))	

print 8462696833 * 71		
