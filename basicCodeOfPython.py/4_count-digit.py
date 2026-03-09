num = int(input("enter a number:"))
count = 0
for i in range(len(str(num))):
    num = num//10
    count += 1
print("number of digits in the number is:", count)
