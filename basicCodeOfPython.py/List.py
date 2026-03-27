import math
num = int(input("how many elements are in the list?\n"))
number =[]

for i in range(num):
    print("Enter the number: ")

for i in range(num):
    number.append(int(input("Enter the number:")))

print("The number in the list:\n")
print(number)
sum=0

for i in range(num):
    sum = sum+ number[i]
    sum1=0
  
print("sum is: ", sum)
mean = sum/num
print("mean is: ",mean)

for i in range(num):
      sum1 = sum1 + pow((number[i]-mean),2)
       
variance = sum1/num
print("variance is: ",variance)
sd= sqrt(variance)
print("The standard deviation is: ",sd)
