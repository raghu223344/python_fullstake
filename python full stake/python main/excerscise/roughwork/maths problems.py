

#finding lcm 


def calculate_lcm(x,y) :
    if x>y:
        greater=x
    else:
        greater=y
    while(True):
        if((greater %x==0) and (greater%y==0)):
            lcm = greater
            break
        greater+=1
        
    return lcm
num1= int (input("enter the number :- "))
num2=int (input("enter the 2nd number:-  "))

print ("the lcm of ",num1,'and',num2,"is",calculate_lcm(num1,num2))