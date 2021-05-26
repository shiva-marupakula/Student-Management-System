dict1={12:13,14:15,16:17}
dict2={2:33,4:44,5:55,6:66}
dict3={7:77,8:88,9:99}
new={}
for i in (dict1,dict2,dict3):
	new.update(i)
print(new,'is concatenation of three dictionaries')
print(len(new),'is lenght of three dictionaries')
