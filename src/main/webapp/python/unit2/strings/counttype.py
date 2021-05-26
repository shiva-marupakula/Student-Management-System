s=input('enter any string')
vc=dc=sc=cc=0
for i in s:
	if(i.isdigit()):
		dc=dc+1
	if(i.isspace()):
		sc=sc+1
	elif(i in ('a','e','i','o','u','A','E','I','O','U')):
		vc=+1
	elif(i.isalpha()):
		cc=cc+1
print('vowel count:{}\n digitcount:{}\n space count:{}\n consonant count:{}'.format(vc,dc,sc,cc))
