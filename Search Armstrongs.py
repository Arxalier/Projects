num = int(input("Enter range to search armstrong numbers: "))
def checkArmstrong(number):
    original_num = number
    sum = 0
    digits = len(str(original_num))
    while number != 0:
        r = number%10
        sum += r**digits
        number = number//10
    if sum==original_num:
        return True
    else:
        return False
for i in range(1,num+1):
    if checkArmstrong(i):
        print(i)