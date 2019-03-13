def rev(n):
	s=0
	while n!=0:
		d=n%10
		s=(s*10)+d
		n=n/10
	return s
	
n=input("Enter a number: ")
copy=n
if rev(n)==copy:
	print copy,"is a Palindrome"
else:
	print copy,"is NOT a Palindrome"
	
