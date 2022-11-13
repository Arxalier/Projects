for i in range(1, 6):
    t = ""
    for j in range(1, i+1):
        t+="* "
    print(t)


for i in range(5, 0, -1):
    t = ""
    for j in range(1,  i+1):
        t+=str(j)+" "
    print(t)

text = "ABCDE"
for i in range(1, 6):
    t = ""
    for j in range(0, i):
        t+=text[j]
    print(t)
