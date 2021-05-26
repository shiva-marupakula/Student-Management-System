# to check whether given number is palindrome
def pali(n):
	p=str(n)
	if(p[::-1]==p):
		print(p,'is palindrome')
	else:
		print(p,'is not a palindrome')
pal=int(input('enter any number'))
pali(pal)

