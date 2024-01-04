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
print("program to perform Arithmetic operation \n")
choice=1
print("1. To perform Addition \n")
print("2. To perform Subtraction \n")
print("3. To perform Multiplication \n")
print("4. To perform Division \n")
print("0. To Exit\n")
while(choice!=0):
 p=int(input("enter a number\n"))
 q=int(input("enter a number\n"))
 choice=int(input("enter a choice\n"))
 if(choice==1):
 print("addition =",add(p,q)) 
elif(choice==2):
 print("subtraction =",sub(p,q))
 elif(choice==3):
 print("multiplication =",mul(p,q))
 elif(choice==4):
 print("division =",div(p,q))
 elif(choice==0):
 break
 else:
 print("Invalid option ")
