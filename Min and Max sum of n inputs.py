text=int(input("Enter a number, to stop giving input enter nothing: "))
sum = 0
min = max = text
while text:
    text=input("Enter a number, to stop giving input press 'x': ")
    if text=='x':
        break
    else:
        text=int(text)
    if text>max:
        max = text
    if text<min:
        min = text
print("Sum of minimum and maximum values are: ", min+max)