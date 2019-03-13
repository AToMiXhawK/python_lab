#GITHIN KOSHY MANESH
#Roll No: 11072
# ----------------------------------------------------------
#| Python Program To Print Prime Numbers Between Two Limits |
# ----------------------------------------------------------
def prime(n):
	if n==1 or n==0:
		return 0
	i=2
	while i<=n/2:
		if n%i==0:
			return 0
		else:
			i+=1
	return n
	
ll=input("Enter the Lower limit: ")
ul=input("Enter the Upper Limit: ")
print "Prime numbers between",ll,"and",ul,"are",
if ll<2: ll=2
for i in range(ll,ul+1):
	if prime(i)!=0:
		print ",",prime(i),
