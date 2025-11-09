# Python Basics
name = input("Enter Your Name : ")
age = int(input("Enter Your Age : "))

next_age = age + 1
print(f"Hi {name}, next year you ll be {next_age} years old.")
print("Welcome to python , Commander!")

# Python variables are dynamically typed the type can be changed for the variables
# Allowed letters , digit , underscores ; must not starts with a digit ; case-sensitive


# Built-in data-types in python are - int , float , bool , str 

a = 20
print(type(a))

# Type Casting

x = str(a)

# this could be the problem unlike js it wont assign NaN it will raise a value error:
z= int(x+"y")
print(type(x))

# Multiple Assignment

g,h,i = 10,20,30
g = h = i = 0
print(g,h,i)

# Mini Practice Challenge # 2

name = input("Enter Your Name : ")
age = int(input("Enter Your Age : "))
height = float(input("Enter Your Height : "))

print(f"{name} is {age} years old and {height} feet tall.")
print(f"Type of name : {type(name)} \nType of age : {type(age)} \nType of height : {type(height)}")

# Strings and String Operations
# String is a sequence of charachters enclosed in quotes. "" , '' , """ """

# Indexing in string
#   A   y   u   s   h
#   0   1   2   3   4
#  -5  -4  -3  -2  -1

name = 'Ayush'
# print(name[ (starting position) : (ending position exclusive) : (steps jumps + means forward jump - means backward jumps) ])
text = "Python"
rev = text[::-1]
print(rev)

# string concat using + operator
# len function len( str ) total count of charachters in the string.
print(name)

# Strings built in power
    # .upper() uppercase
    # .lower() lowercase
    # .title() capitalize
    # .replace(old , new) replace old text with new
    # .find(part_of_string) returns starting position [index]
    # .count(char) returns the count of charachter in a string
    # .split(breaker) splits string into the list on basis of breaker 
    # .strip() remove spaces both leading and trailing // also comes with .lstrip() leading .rstrip() trailing 
    # "joiner".join(list) join each element of list with the joiner !important : each element inside the list should be type string
    
# Escape Sequences
print("Hello\nWorld") # newline
print("Hello\tWorld") # tab
print("I\'m Ayush")   # single quote
print("Path: C:\\Users\\Ayush") # backslash

# raw strings
path = r"c:\Users\Ayush"
print(path)

# formatting numbers
pi =3.14159265
print(f"Pi rounded = {pi:.2f}")

# Mini Practice Challange #3

fName = input("Enter the first name : ").strip()
lName = input("Enter the last name : ").strip()
fullName = " ".join([fName.title(), lName.title()])
print(f"Full name: {fullName}")
print(f"Total letters: {len(fullName)-1}")
print(f"Initials: {fName[0]+'.'+lName[0]}.")

# Operators :
a = 10
b = 3

print(a + b)   # Addition → 13
print(a - b)   # Subtraction → 7
print(a * b)   # Multiplication → 30
print(a / b)   # Division (float) → 3.333...
print(a // b)  # Floor Division (no decimals) → 3
print(a % b)   # Modulus (remainder) → 1
print(a ** b)  # Exponentiation → 10³ = 1000

x = 5
y = 10

print(x == y)   # False
print(x != y)   # True
print(x > y)    # False
print(x < y)    # True
print(x >= 5)   # True

a = True
b = False

print(a and b)   # False
print(a or b)    # True
print(not a)     # False

# Assignment Operators

x = 5
x += 2   # same as x = x + 2
x -= 1
x *= 3
x /= 2
x **= 2
x //= 2

# Membership Operators

name = "MasterChief"
print("Chief" in name)   # True
print("Halo" not in name)  # True

# Identity Operator

x = 10
y = 10

z = x

print(z is x) # True both pointing same address
print(z is not x) # false cuz z and x are same memory reference
print(y == x) # true cuz both has same value
print(y is x) # false despite having the same value both are different memory address.


# Ternary Operator

x = 10
result = "Even" if x % 2 == 0 else "Odd"
print(result)

# Mini Practice Challange #5

x , y = int(input("Enter the first number : ")) , int(input("Enter the second number : "))
print(f"Sum : {x+y}\n"
      f"Difference : {x-y}\n"
      f"Product : {x*y}\n"
      f"quotient : {x/y:.2f}\n")

if x == y :
    print("Both numbers are equal")
elif x > y:
    print("x is greater than y")
else:
    print("y is greater than x")

num = int(input("Enter the number:"))
print(f"{num} is an {"even" if num % 2 == 0 else "odd"} number.")
    