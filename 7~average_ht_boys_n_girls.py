bc=0
gc=0
bs=0
gs=0
n=0
count=input("Enter the Count: ")
while n<count:
	g=raw_input("Enter the gender: ")
	if g=='m':
		bs+=input("Enter the Height: ")
		n+=1
		bc+=1
	elif g=='f':
		gs+=input("Enter the Height: ")
		n+=1
		gc+=1
	else:
		print "invalid Input"
abht=float(bs)/float(bc)
aght=float(gs)/float(gc)
print "Average height of Boys = ",abht
print "Average height of Girls = ",aght

