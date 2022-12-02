# Arxalier's Death Valley
def solve(expression: str):
    question = expression.replace("÷", "/").replace("×", "*").replace(" ", "").replace("{", "(").replace("}", ")")
    terms = []
    t = ""
    for character in str(question + "+"):
        t += character
        if character in "*/+-^()":
            terms.append(t[0:-1])
            terms.append(character)
            t = ""
    while '' in terms:
        terms.remove("")
    del terms[-1]

    def solveExpression(values: list) -> list:  # Returns solution of expression without parentheses in it
        for i in range(len(values) - 1, -1, -1):
            if values[i] == "^":
                values[i] = float(values[i - 1]) ** float(values[i + 1])
                del values[i + 1]
                del values[i - 1]
        for i in range(len(values) - 1, -1, -1):
            if values[i] == "/":
                values[i] = float(values[i - 1]) / float(values[i + 1])
                del values[i + 1]
                del values[i - 1]
        for i in range(len(values) - 1, -1, -1):
            if values[i] == "*":
                values[i] = float(values[i - 1]) * float(values[i + 1])
                del values[i + 1]
                del values[i - 1]
        for i in range(len(values) - 1, -1, -1):
            if values[i] == "+":
                values[i] = float(values[i - 1]) + float(values[i + 1])
                del values[i + 1]
                del values[i - 1]
        for i in range(len(values) - 1, -1, -1):
            if values[i] == "-":
                values[i] = float(values[i - 1]) - float(values[i + 1])
                del values[i + 1]
                del values[i - 1]
        return values[0]

    while "(" in terms:
        for indice1 in range(len(terms)):
            if terms[indice1] == ")":
                endIndex = indice1
                for indice2 in range(indice1, -1, -1):
                    if terms[indice2] == "(":
                        startIndex = indice2
                        break
                break
        ans = solveExpression(terms[startIndex + 1:endIndex])
        terms.insert(startIndex, ans)
        del terms[startIndex + 1:endIndex + 1]
    terms = solveExpression(terms)
    return terms


from tkinter import *

root = Tk()
root.title("Calculator")
out = Entry(root, width=30, borderwidth=10)
out.grid(row=0, column=0, columnspan=5)


def button_add(number):
    out.insert(1000, number)


def equate():
    x = solve(out.get())
    out.delete(0, END)
    out.insert(0, x)


def clear():
    out.delete(0, END)


def back():
    x = out.get()[0:-1]
    out.delete(0, END)
    out.insert(0, x)


button_0 = Button(root, text="0", padx=20, pady=10, command=lambda: button_add("0"))
button_1 = Button(root, text="1", padx=20, pady=10, command=lambda: button_add("1"))
button_2 = Button(root, text="2", padx=20, pady=10, command=lambda: button_add("2"))
button_3 = Button(root, text="3", padx=20, pady=10, command=lambda: button_add("3"))
button_4 = Button(root, text="4", padx=20, pady=10, command=lambda: button_add("4"))
button_5 = Button(root, text="5", padx=20, pady=10, command=lambda: button_add("5"))
button_6 = Button(root, text="6", padx=20, pady=10, command=lambda: button_add("6"))
button_7 = Button(root, text="7", padx=20, pady=10, command=lambda: button_add("7"))
button_8 = Button(root, text="8", padx=20, pady=10, command=lambda: button_add("8"))
button_9 = Button(root, text="9", padx=20, pady=10, command=lambda: button_add("9"))
button_add_key = Button(root, text="+", padx=19, pady=10, command=lambda: button_add("+"))
button_subtract_key = Button(root, text="-", padx=20, pady=10, command=lambda: button_add("-"))
button_multiply_key = Button(root, text="*", padx=20, pady=10, command=lambda: button_add("*"))
button_divide_key = Button(root, text="/", padx=20, pady=10, command=lambda: button_add("/"))
button_equate_key = Button(root, text="=", padx=20, pady=10, command=lambda: equate())
button_decimal_key = Button(root, text=".", padx=20, pady=10, command=lambda: button_add("."))
button_clear = Button(root, text="Clear", padx=20, pady=10, command=lambda: clear())
button_back = Button(root, text="Backspace", padx=40, pady=10, command=lambda: back())
button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)
button_0.grid(row=4, column=0)
button_decimal_key.grid(row=4, column=1)
button_equate_key.grid(row=4, column=2)
button_add_key.grid(row=1, column=4)
button_subtract_key.grid(row=2, column=4)
button_multiply_key.grid(row=3, column=4)
button_divide_key.grid(row=4, column=4)
button_back.grid(row=5, column=0, columnspan=2)
button_clear.grid(row=5, column=2, columnspan=4)
root.mainloop()
