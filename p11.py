def count_characters(filename):
#Open the file in read mode
 with open(filename,"r") as file:
 #Read the contents of the file into a string
 contents = file.read()
# Create an empty dictionary
 char_count = {}
#Loop through each character in the string 
 for char in contents:
# If the character is already in the dictionary, increment its count by 1
 if char in char_count:
 char_count[char] += 1
# If the character is not in the dictionary, add it and set its count to 1
 else:
 char_count [char] = 1
# Return the dictionary
 return char_count
# Input the data
data = input("Enter the data: ")
# Input the filename to be saved
filename = input("Enter the filename to save the data: ")
#Write the data to the file
with open(filename, "w") as file:
 file.write(data)
 #Inform that the file is being opened for reading
print("Opening the file '" + filename + " for reading...")
# Call the function and store the result in a variable
result = count_characters(filename)
# Print the result
print("Character frequency in " + filename + " is : \n" + str(result)) 
