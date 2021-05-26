#to create dictionary with friends date of birth and print them in asorted order
mydict={'sainath':'23-06-2001','rakesh':'9-11-2001','shiva':'10-05-2002','adarsh':'11-4-2000','kalyan':'02-12-1999'}
print(sorted(mydict.items()),'is sorted dictionary of items')
name=input('enter your friend name')
if(name in mydict):
	print(mydict[name],'is your friend',name,'date of birth')
else:
	dob=input('enter your friend date of birth in (01-01-2001) format')
	mydict[name]=dob
print(mydict)
