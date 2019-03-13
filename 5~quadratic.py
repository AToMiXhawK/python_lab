a = input("Enter the value of a: ")
if a==0:
	print "value of a should not be zero"
else:
	b = input("Enter the value of b: ")
	c = input("Enter the value of c: ")
	d=b*b-4*a*c
	import math
 	if d==0:
		r=-b/2*a
		print "Roots are REAL and EQUAL and it is",r
	elif d>0:
		x=math.sqrt(d)
		r1=(-b+x)/2*a
		r2=(-b-x)/2*a
		print "Roots are REAL and UNEQUAL and they are",r1,"and",r2
	else:
		x=math.sqrt(-d)
		re=-b/2*a
		img=x/2*a
		print "Roots are COMPLEX and they are"
		print re,"+",img,"i and"
		print re,"-",img,"i"

		  
