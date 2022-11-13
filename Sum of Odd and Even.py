Lower_Limit = int(input("Enter lower limit (including): "))
Upper_Limit = int(input("Enter upper limit (including): "))
Sum_Even, Sum_Odd = 0, 0
if Lower_Limit%2==0:
    for i in range (Lower_Limit, Upper_Limit+1,2):
        Sum_Even+=i
    for i in range (Lower_Limit+1, Upper_Limit+1,2):
        Sum_Odd+=i
else:
    for i in range (Lower_Limit, Upper_Limit+1,2):
        Sum_Odd+=i
    for i in range (Lower_Limit+1, Upper_Limit+1,2):
        Sum_Even+=i
print("Sum of odd numbers between limits is ", Sum_Odd)
print("Sum of even numbers between limits is ", Sum_Even)

# 1, 10 = 1 2 3 4 5 6 7 8 9 10 = 1+3+5+7+9 = 25, 2+4+6+8+10 = 30
# Result: Sum_Even = Sum_Odd + ceil((Upperlimit-Lowerlimit)/2)