n=input("Enter The Count: ")
if n<1:
	print "Count must be >0"
elif n==1:
	print "0"
elif n==2:
	print "0, 1"
else:
	first =0
	second =1
	print 0, 1,
	i=3
	while i<=n:
		third=first+second
		print third,
		first = second
		second = third
		i+=1
	
