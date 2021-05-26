# methods of strings
#capatalise method: which converts first letter of string into capatal
s='shiva marupakula'
print(s.capitalize())
# title method
print(s.title())
#upper method
print(s.upper())
#lower method
print(s.lower())
# isupper method 
print(s.isupper())
#islower method
print(s.islower())
#isdigit method
print(s.isdigit())
# isspace method
print(s.isspace())
#isalpha method
print(s.isalpha())
#lenght method
print(len(s))
#index method
print(s.index('u'))
#find method
print(s.find('shiva'))
#rfind whic returns index of last occurance
print(s.rfind('marupakula'))
# count method
print(s.count('a'))
print(s.count('p',0,5))
#swapcase method 
print(s.swapcase())
#split method
mylist=s.split()
print(mylist)
mylist=s.split('a',2)
print(mylist)
# join method
j=' '.join(mylist)
print(j)
#startswith method
print(s.startswith('s'))
#endswith method
print(s.endswith('la'))
#replace method
print(s.replace('marupakula','ias'))

