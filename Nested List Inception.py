n = int(input("Enter number of lists required: "))
start = ["a"]
for i in range(1, n):
    b = []
    b.append(start)
    start = b
print(start)
# Part 2
goFurther = True
index = 0
x = [i for i in start]
c = 0
while goFurther:
    if type(x[0])==type([]):
        c+=1
        y = x[0]
        x = y
    else:
        goFurther = False
newList = ['b']
for i in range(1, c+1):
    d = []
    d.append(newList)
    newList = d
print(newList)


