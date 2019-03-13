n=input("Enter a number: ")
amst=0
cpy=n
s=0
x=1
d=[]
while n/10!=0:
	x=x+1
	d.append(n%10)
	n=(n/10)-((n%10)/10)
d.append(n)
y=1
while y<=x:
	amst=amst+(d[y-1]**x)
	y=y+1
	
if amst==cpy:
	print cpy,"is an Armstrong Number"
else:
	print cpy,"is NOT an Armstrong Number"
	
