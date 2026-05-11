S1 = "  Welcome   "
print(S1.strip())
text = "python programming"

print(text.upper())   # PYTHON PROGRAMMING
print(text.lower())   # python programming
print(text.title())   # Python Programming
print(text.capitalize())  # Python programming

text = "  hello  "

print(text.strip())    # removes both sides spaces
print(text.lstrip())   # left side
print(text.rstrip())   # right side

pi   = 3.14159
name = "Python"
print(f"Value of pi = {pi:.2f}")       # 2 decimal places
print(f"{name} is awesome!")
print("Hello {:>10}".format(name))     # right-align width 10
print(f"{2**10} = 2^10")               # expression in f-strin

print("A", "B", "C", sep="-")       # A-B-C
print("Loading", end="...")          # no newline
print("Done")
print(f"{"Name":<10} {"Score":>5}")
print(f"{"Rashna":<10} {95:>5}")
