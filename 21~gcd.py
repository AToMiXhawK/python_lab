a=input("Enter the value of a: ")
b=input("Enter the value of b: ")
i=1
while (not(i>a or i>b)):
	if (a%i==0 and b%i==0):
		gcd=i
	i=i+1
print "GCD of",a,"and",b,"is",gcd
