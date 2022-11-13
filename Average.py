total=0
for i in range(1, 11):
    text="Enter number "+str(i)+": "
    num=float(input(text))
    total+=num
print("Total is ", total)
print("Average is ", total/10)
    