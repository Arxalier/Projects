# Arxalier's BADMAS Calculator
# Yes, BADMAS. Please do not use this under any circumstances. It is not reliable.
# KNOWN LIMITATIONS:
# Program gets multiple seizures when you try something like 1-(-1), instead use 1-(0-1)
# 1+(1) works though
# Just don't put a single negative term in brackets or start a bracket with a negative term
# 1-2^2 = -3, right? WRONG. My code disagrees. It runs on its own brain. I have given up on teaching it BODMAS.
# Please do not use negative sign next to an exponent. Use brackets like 1-(2^2)
def calculate(s: str) -> int:
    question = s.replace("÷","/").replace("×","*").replace(" ","").replace("{","(").replace("}",")")
    terms = []
    t = ""
    for character in str(question + "+"): # The source of all errors. This shabby code cannot be explained.
        t += character # Basically its trying to separate each operator and number
        if character in "*/+-^()":
            terms.append(t[0:-1])
            terms.append(character)
            t = ""
    del terms[-1] # An extra + is added to fix bugs im too lazy to solve. This plus is now deleted
    for term in range(len(terms)):
        if terms[term] == "-" and terms[term + 1].isnumeric(): # Turns 1-2 into 1+(-2)
            terms[term + 1] = terms[term]+terms[term+1]
            if terms[term-1] == "(": terms[term]=""
            else: terms[term]="+"
    while '' in terms:
        terms.remove("") # Removes empty spaces which my terrible code utilises
    print(terms)
    def solveExpression(values: list) -> list:  # Returns solution of expression without parentheses in it
        for i in range(len(values) - 1, -1, -1): # This is the saddest part. It checks backwards to avoid displacing all
            if values[i] == "^": # other indices
                values[i] = float(values[i - 1]) ** float(values[i + 1])
                del values[i + 1]
                del values[i - 1]
                print(values)
        for i in range(len(values) - 1, -1, -1):
            if values[i] == "/":
                values[i] = float(values[i - 1]) / float(values[i + 1])
                del values[i + 1]
                del values[i - 1]
                print(values)
        for i in range(len(values) - 1, -1, -1):
            if values[i] == "*":
                values[i] = float(values[i - 1]) * float(values[i + 1])
                del values[i + 1]
                del values[i - 1]
                print(values)
        # Addition and Subtraction
        for i in range(len(values) - 1, -1, -1):
            if values[i] == "+":
                values[i] = float(values[i - 1]) + float(values[i + 1])
                del values[i + 1]
                del values[i - 1]
                print(values)
        for i in range(len(values) - 1, -1, -1):
            if values[i] == "-":
                values[i] = float(values[i - 1]) - float(values[i + 1])
                del values[i + 1]
                del values[i - 1]
                print(values)
        return values
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
        terms[startIndex:endIndex + 1] = ans
    terms = solveExpression(terms)
    print(terms)
    return terms
a = input()
try:
    a = calculate(a)
except:
    print(a)
