print("program to check positive or negative ")
choice = 1
while(choice != 0):
    print("enter a number ")
    a = int(input())
    if a > 0:
        print(a, "is a positive number ")
    else:
        print(a, "is a negative number")
    print("Enter 1 to continue and 0 to exit ")
    choice = int(input()) 
