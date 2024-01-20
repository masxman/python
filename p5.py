def add(a,b):
    x=(a+b)
    return x

def sub(a,b):
    x=(a-b)
    return x

def mul(a,b):
    x=(a*b)
    return x

def div(a,b):
    x=(a/b)
    return x

print("Program to perform Arithmetic operation \n")
choice=1
print("1. To perform Addition \n")
print("2. To perform Subtraction \n")
print("3. To perform Multiplication \n")
print("4. To perform Division \n")
print("0. To Exit\n")

while(choice!=0):
    p=int(input("Enter a number\n"))
    q=int(input("Enter a number\n"))
    choice=int(input("Enter a choice\n"))
    if(choice==1):
        print("Addition =",add(p,q)) 
    elif(choice==2):
        print("Subtraction =",sub(p,q))
    elif(choice==3):
        print("Multiplication =",mul(p,q))
    elif(choice==4):
        print("Division =",div(p,q))
    elif(choice==0):
        break
    else:
        print("Invalid option ")
