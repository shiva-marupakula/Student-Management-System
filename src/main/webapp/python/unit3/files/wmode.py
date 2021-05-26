myfile=open('file1.txt','w+')
myfile.write('shivamarupakulakalammargukt basar')
myfile.writelines(['shiva\n','marupakula\n','kalamma\n','rgukt basar\n'])
print(myfile.read())
print(myfile.tell())
myfile.seek(0)
print(myfile.tell())
print(myfile.readline())
print(myfile.readlines())


