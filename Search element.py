lst = eval(input("Enter list/tuple: "))
elem = eval(input("Enter element to search: "))
indices = []
for i in range(0, len(lst)):
    if lst[i] == elem:
        indices.append(i)
if indices:
    print("Element found in the following indices of given list:", indices)
else:
    print("No such element found in given list")