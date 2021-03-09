# Get list of values from the user
user = [] #initializing list
n = 0
while n < len(seq):
    user.append(input("Print DNA value, all numbes at once, please: ")) # adding value to the list
    n += 1
print(user)

# Search through items in list of dictionary
for name,value in dic.items():
    if user == value:
        print(name)
        exit(0)
    else:
        continue
print("Not found")