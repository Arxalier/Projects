num = input("Enter a number: ")
digit = input("Which digit would you like to check: ")
count = 0
for i in num:
    if digit==i:
        count+=1
print(digit+" occurs in the given number "+str(count)+" times.")