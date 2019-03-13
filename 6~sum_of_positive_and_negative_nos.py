psum=0
nsum=0
count=input("Enter the count: ")
for n in range(0,count):
	num=input("Enter the Number: ")
	if num>=0:
		psum+=num
	else:
		nsum+=num
	n=n+1
print "Sum of Positive Numbers is :",psum
print "Sum of Negative Numbers is :",nsum
