num = float(input("Enter number to find square root of:  "))
accuracy = 100
minimum = 1
maximum = num // 2 + 1
for i in range(accuracy):
    mean = (minimum + maximum) / 2
    square = mean** 2
    if square > num:
        maximum = mean
    elif square < num:
        minimum = mean
print(mean)
