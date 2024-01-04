#creating dictonary
dict = {1:"Python",2: "CN",3:"OS"}
print(dict)
#adding elements to dictonary
dict["4"] = "CA"
print("Updated Dictionary:\n",dict)
#The get() method returns the value of the item with the specified key.
x = dict.get(3)
print(x)
#changing values in dictonary
dict[2] = "SQL" 
print(dict)
#finding number of items i.e key value pairs present in dictonary
print(len(dict)) 
