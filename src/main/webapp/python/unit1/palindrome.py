#to check whether given number is or palindrome not.
n=int(input("enter any number"))
s=0
temp=n
while(n!=0):
	r=n%10
	s=(s*10)+r
	n=n//10
print(s,'is reverse of num')
if(temp==s):
	print('number is palindrome')
else:
	print('number is not palindrom')
