def add(n1,n2):
    return n1+n2
def multiplication(n1,n2):
    return n1*n2
def minus(n1,n2):
    return n1-n2
def divide(n1,n2):
    if n2==0:
        return"not avelapel  operation"
    return n1/n2
i=1
while(True):
    
    print("My calculator ")
    if i==1:
        try:
            num1=int( input("enter the first number\n"))
        except:
            print("its not a number")    
    op=input("enter your operation:\n1- (*)\n2-(-)\n3-(+)\n4-(/)\nenter 0 to stop\n")
    try:
        num2=int( input("enter the second number\n"))
    except:
        print("its not a number")
    
    if op=="1"or op=="*": 
        num1=multiplication(num1,num2)
        print("=",num1)
    elif op=="2"or op== "-":
        num1=minus(num1,num2)
        print("=",num1)
    elif op=="3"or op=="+": 
        num1=add(num1,num2)
        print("=",num1)
    elif op=="4"or op=="/": 
        num1=divide(num1,num2)
        print("=",num1)
    elif op=="0":
        print("=",num1)
        break
    else :
        print("envalied choice try agean")
    i+=1







