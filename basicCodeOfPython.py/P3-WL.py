# to reverse a number using while loop
n = int(input("Enter a number:"))
original = n
reverse = 0
while n > 0:
    digit = n%10
    reverse = reverse*10 +digit
    n = n//10

print(f"The reverse of {original} is: {reverse}")

  