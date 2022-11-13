import matplotlib.pyplot as plt
degree = int(input("Enter degree of polynomial: "))
coefficients = []
for i in range(1, degree+2):
    text = "Enter coefficient of x^" + str(degree+1-i) +": "
    coefficient = int(input(text))
    coefficients.append(coefficient)
def f(x, _coefficients):
    value = 0
    deg = len(_coefficients)-1
    for _coefficient in _coefficients:
        value += _coefficient*(x**deg)
        deg -= 1
    return value
numbers = []
values = []
for num in range(-300, 300):
    val = num/10
    numbers.append(val)
    values.append(f(val, coefficients))
plt.plot(numbers, values)
deg = len(coefficients) - 1
polynomial = ""
for k in coefficients:
    if k>0:
        polynomial += str(k)+"x^"+str(deg)+"+"
    else:
        polynomial += "("+str(k)+")"+"x^"+str(deg)+"+"
    deg -= 1
plt.title(polynomial.rstrip("x^0+"))
plt.show()