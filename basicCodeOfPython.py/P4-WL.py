# to reverse a number using a while loop and to check whether the number is palindrome or not
n = int(input("enter a number:"))
original =0
reverse =0
while n >0:
    digit = n %10
    reverse =reverse*10+digit
    n = n//10
print(f"The reverse of {original} is: {reverse}")
if original == reverse:
    print(f"{original} is a palindrome.")
else:
    print(f"{original} is not a palindrome.")