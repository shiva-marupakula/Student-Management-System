# to calculate bill amount for item.
a=input("enter item name")
b=float(input("enter the quantity"))
p=float(input('enter price of item'))
d=float(input('enter the discount'))
tp=(b*p)
dis=tp*(d/100)
g=tp-dis
print ("*******************BILL**********************")
print ("item name\tquantity\tprice\tdiscount")
print ("{}\t	{}\t	{}\t    {}".format(a,b,p,d))
print ('total price is ',g)
print('***************PLEASE VISIT AGAIN**************')
