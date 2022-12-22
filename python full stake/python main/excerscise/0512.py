items=[]
totalamount=[]




def swiggy() :
    print("select the item menu: ")
    print("1.dosa")
    print("2.burger")
    print("3.pizza")
    print("4.chicken")
    n=int(input("select the number: "))
    if(n>0 and n<5) :
        if(n==1):
            dosa("dosa",50) 
        elif(n==2):
            burger("burger",150)
        elif(n==3):
            pizza("pizza",150)
        elif(n==4):
            chicken("chicken",150)
        elif(n==5):
            burger("burger",150)
                
print("welcome to swiggy")
swiggy()