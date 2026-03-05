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
