n=input("Enter the Count: ")
big=input("Enter The First Number: ")
for i in range(1,n):
	num=input("Enter The next Number: ")
	if num>big:
		big=num
print "The largest among the given numbers is:",big
