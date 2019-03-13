def rev(n):
	s=0
	while n!=0:
		d=n%10
		s=(s*10)+d
		n=n/10
	return s
n=input("Enter a number: ")
print "The Reverse of the given Number is",rev(n)
                                                                                                                         
