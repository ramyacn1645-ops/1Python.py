num = int(input("enter a number"))
sequence =[]
while num != 1:
    if num %2 ==0:
        num = num//2
    else:
        num = 3*num+1 
        print(num)

    sequence.append(num)
print(sequence)