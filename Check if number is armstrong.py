num = int(input("Enter number to check if it is armstrong: "))
original_num = num
sum = 0
digits = len(str(num))
while num != 0:
    r = num%10
    sum += r**digits
    num = num//10
if sum==original_num:
    print("Given number is armstrong.")
else:
    print("Given number is not armstrong.")