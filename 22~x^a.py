def exp(x,a):
	p=1
	if a>=0:
		for i in range(0,a):
			p*=x
	else:
		for i in range(0,(-a)):
			p=float(p)/x
	return p

x=input("Enter the value of x: " )
a=input("Enter the value of a: " )
print x,"Raised to the power",a,"is",exp(x,a)
