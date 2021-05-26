# to replace the content 
f1=open('iiit.txt','r+')
s=f1.read()
d=s.replace('line','IIIT')
f1.seek(0)
f1.write(d)
f1.close()
