#to copy the content of one file to anotherfile
f1=open('shiva.py','r')
f2=open('ssmarupakula.py','w')
cont=f1.read()
f2.write(cont)
f1.close()
f2.close()

