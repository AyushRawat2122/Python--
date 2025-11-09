# Loops 
for i in range(0,11,2): # range(start, stop, step)
    print(i)
# Mini Practice #1

# 1️⃣ Print numbers from 1 to 10.
# 2️⃣ Print all even numbers between 1–20.
# 3️⃣ Print countdown from 10 to 1.
# 4️⃣ Print each letter of your name.
# 5️⃣ Sum all numbers from 1–50.

for i in range(1,11):
    print(i , end = " ")

for i in range(2,21,2):
    print(i , end = " ")

for i in range(10,0,-1):
    print(i , end = " ")

for char in "Ayush" :
    print(char , end = " ")

i = 50
total = 0
while i > 0 :
    total+=i
    i-=1
print(total)

# enumerate(list) returns index, fruit

fruits = ["apple","banana","mango"]
for idx , fruit in enumerate(fruits):
    print(idx , fruit)

def printPyramid(rows) :
    cols = 2 * rows - 1
    for i in range(rows):
        n=1
        for j in range(cols):
            if(j <= cols//2 + i  and j >= cols//2 - i ):
                print(n,end="")
                if j >= cols//2:
                    n-=1
                else:
                    n+=1 
            else:
                print(" ",end="")
        print("\n",end="")

printPyramid(5)

def printHollow(rows) :
    cols = 2 * rows - 1
    for i in range(rows):
        for j in range(cols):
            if(j == cols//2 + i  or j == cols//2 - i ):
                print("*",end="")
            else:
                print(" ",end="")
        print("\n",end="")
        
    for i in range(rows-2,-1,-1):
        for j in range(cols):
            if(j == cols//2 + i  or j == cols//2 - i ):
                print("*",end="")
            else:
                print(" ",end="")
        print("\n",end="")

printHollow(5)