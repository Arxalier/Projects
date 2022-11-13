import matplotlib.pyplot as plt
maxNum = 10000
numbers = []
stepCount = []
for i in range(1, maxNum + 1):
    steps = 0
    num = i
    numbers.append(i)
    while num != 1:
        if num % 2 == 0:
            num = num / 2
        else:
            num = 3 * num + 1
        steps += 1
    stepCount.append(steps)
plt.plot(numbers, stepCount)
plt.show()
