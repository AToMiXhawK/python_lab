def layers(n):
	l= n%100000
	f= n/100000
	n2= l*10+f
	return n2
print ""
print ""
print "+----------------!!!!PUZZLE!!!!----------------+"
print ""
num=raw_input("  Enter your solution to the puzzle: ")
print ""
print ""
if (str.isdigit(num) and len(num)==6):
	n=int(num)
	n2 = layers(n)
	if (n*3)==n2:
		print "+-----Congrats!! You Found The Solution!!!-----+"
		print ""
		print ""
		
	else:
		print "----------------!! TRY AGAIN !!----------------+"
		print ""
		print ""
	
else:
	print "Invalid Input!! Enter a six digit number"
	print ""
	print ""
