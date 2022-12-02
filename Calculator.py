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
q = input("Enter expression: ")
print(solve(q))