name=open('names.txt')
mesg=open('msg.txt')
msg=mesg.read()
for i in name:
	mail='hello'+i+msg
	mymail=open(i+'.txt','w')
	mymail.write(mail)
	mymail.close()
name.close()
mesg.close()
