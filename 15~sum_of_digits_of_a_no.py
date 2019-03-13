def sum(n):
	s=0
	while n!=0:
		d=n%10
		s=s+d
		n=n/10
	return s
	
n=input("Enter a number: ")
print "The Sum of Digits of the given Number is",sum(n)

