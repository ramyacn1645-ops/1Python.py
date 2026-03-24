def compare_three_nums(a,b,c): #function defination
  if(a>b and a>c):
    print(a,"is greater)
  elif(b>c):
    print(b,"is greater)
  else:
    print(c,"is greater)

a = int(input("enter the value of a:"))
b = int(input("enter the value of b:"))
c = int(input("enter the value of c:"))
print("the greatest of three number is ",compare_three_nums(a,b,c))  #function calling

# Another method
a = int(input("enter the value of a:"))
b = int(input("enter the value of b:"))
c = int(input("enter the value of c:"))

if(a>b and a>c):
    print(a,"is greater)
  elif(b>c):
    print(b,"is greater)
  else:
    print(c,"is greater)

# hike the salary based on their current salary 
num = int(input("Enter the number of employee"))
salary =[]
print(f"Enter {num} employees salary")
for i in range(num):
    salary.append(float(input("Enter salary: ")))
print(salary)
for i in salary:
    if salary>= 50000:
        salary = salary + salary*0.2
    else:
        salary = salary + salary*0.3
print(" updated salary is: ", salary)
    
