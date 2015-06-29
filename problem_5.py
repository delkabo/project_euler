#Smallest multiple
#Problem 5

#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# Not have answer the question


"""
v = 1
number_try = False
lines = "----------------------|"
while number_try == False:
	z = 0
	c = 0
	for b in range(1, 11):
		if v % b == 0:
			c += 1
			z += v/b
			print str(c) + " " + str(v / b)
			if c == 10:
				print lines
				print z
				print lines
				print v
				number_try = True
				break
	v += 1

print lines
print
print "Hello"
"""
"""
do = int(input("Enter number, please: "))

if do <= 13:
	v = 1
	number_try = False
	lines = "----------------------|"
	while number_try == False:
		z = 0
		c = 0
		for b in range(1, do + 1):
			if v % b == 0:
				c += 1
				print  "Number# " + str(c) + ": " +str(v) + " / " + str(b) + " = " + str(v / b)
				if c == do:
					print lines
					print v
					number_try = True
		v += 1

print lines
print
print "Hello"
"""

#version two

num = int(input("Enter the number "))
step = 1
level = num

timer = 0

while level > 0:
	
	timer += 1
	
	answer = ((num * step)/level) * level
	
	
	if level -1 != 0 and ((num * step)/(level - 1)) * (level-1) == answer:
		level -= 1
	else:
		step += 1
		level = num
	print
	print level
	print
		
	if level == 1:
		print "This number: " + str(answer)	
		break
		
	if timer > 100000000000:
		print "Problem with you code"
		break		

# fo number 20 answer = 232792560
