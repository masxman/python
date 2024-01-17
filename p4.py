dict = {1:"Python",2: "CN",3:"OS"}
print(dict)

dict["4"] = "CA"
print("Updated Dictionary:\n",dict)

x = dict.get(3)
print(x)
#changing values in dictonary
dict[2] = "SQL" 
print(dict)
#finding number of items i.e key value pairs present in dictonary
print(len(dict)) 
