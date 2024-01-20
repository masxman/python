def count_characters(filename):
    with open(filename,"r") as file:
        contents = file.read()
    char_count = {}
    for char in contents:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

data = input("Enter the data: ")
filename = input("Enter the filename to save the data: ")

with open(filename, "w") as file:
    file.write(data)

print("Opening the file '" + filename + " for reading...")
result = count_characters(filename)
print("Character frequency in " + filename + " is : \n" + str(result)) 
