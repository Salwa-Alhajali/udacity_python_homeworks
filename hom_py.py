def add():
    num1=int( input("enter the first number\n"))
    num2=int( input("enter the second number\n"))
    return num1+num2
def multiplication():
    num1=int( input("enter the first number\n"))
    num2=int( input("enter the second number\n"))
    return num1*num2
def minus():
    num1=int( input("enter the first number\n"))
    num2=int( input("enter the second number\n"))
    return num1-num2
def divide():
    num1=int( input("enter the first number\n"))
    num2=int( input("enter the second number\n"))
    if num2==0:
        return"not avelapel  operation"
    return num1/num2
while(True):
    print("My calculator ")
    op=input("enter your operation:\n1- (*)\n2-(-)\n3-(+)\n4-(/)\nenter 0 to stop\n")
    if op=="1"or op=="*": 
        print(multiplication())
    elif op=="2"or op== "-": 
        print(minus())
    elif op=="3"or op=="+": 
        print(add())
    elif op=="4"or op=="/": 
        print(divide())
    elif op=="0":
        break
    else :
        print("envalied choice try agean")
        continue






