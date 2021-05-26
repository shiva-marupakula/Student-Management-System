# to print length of each word in given string 
mystring='rajiv gandhi university of knowledge and technologies'
word=mystring.split(' ')
mylist=list(word)
a=map(lambda x:(x,len(x)),mylist)
s=(list(a))
print(dict(s))
