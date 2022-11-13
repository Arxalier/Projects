lst = eval(input("Enter list: "))
newList = []
if len(lst)%2==1:
    y = lst.pop()
while len(lst)!=0:
    x = lst.pop(1)
    newList.append(x)
    x = lst.pop(0)
    newList.append(x)
if len(lst)%2==0:
    newList.append(y)
print(newList)