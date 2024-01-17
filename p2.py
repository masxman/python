my_list = ['Python', 'CN', 'OS', 'CA']
print("Elements of the list, my list are:")
print(my_list)

my_list.insert(2, 'SQL')
print("inserting SQL at index 2 :", my_list)

my_list.remove('CN')
print("removing computer networks from list ", my_list)

my_list.append('BCA')
print("appending BCA to the list", my_list)

print("length of the items in the list ", len(my_list))

x = my_list.pop(0)
print("popped element=", x)
print(my_list)

my_list.clear()
print(my_list)
