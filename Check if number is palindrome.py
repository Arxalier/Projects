n = int(input("Enter a number to check palindrome of: "))
original_number = n
r = 0
rev = 0
while n!=0:
    r=n%10
    rev=(rev*10)+r
    n=n//10
if original_number == rev:
    print("Given number is a palindrome.")
else:
    print("Given number is not a palindrome.")