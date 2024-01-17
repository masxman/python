def even(x):
    return x % 2 == 0

a = [1,2,3,4,5,10,13,16]
result = filter(even,a)

print('Original list:', a)
print('Filtered list :', list(result))
