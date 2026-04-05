def area(width, length):
    # function defination 
    return width*length

width = int(input("Enter the width of the rectangle:"))
length = int(input("Enter the length of the rectangle:"))
try:
    result = area(width,length)
    print(f"The area of the rectangle is: {result}")

except ValueError:
    print("Please enter valid numbers for width and length.")
