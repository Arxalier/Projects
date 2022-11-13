text = input("Enter string: ")
vowels = consonants = uppers = lowers = 0
for letter in text:
    if letter.isalpha():
        if letter in "aeiou":
            vowels+=1
        else:
            consonants+=1
        if letter.isupper():
            uppers+=1
        else:
            lowers+=1
print("Vowels in string are", vowels)
print("Consonants in string are", consonants)
print("Upper case characters in string are", uppers)
print("Lower case characters in string are", lowers)