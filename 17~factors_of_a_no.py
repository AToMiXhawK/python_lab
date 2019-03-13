def factors(n):
	print "The factors of",n,"are:",
	x=1
	while x<=n/2:
		if n%x==0:
			print x,",",
		x=x+1
	else:
		print "and",n
	return
	
n=input("Enter a Number: ")
factors(n)

