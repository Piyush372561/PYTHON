#PRACTICE SHEET 1 OF PYTHON TUTORIAL
#w a p to input 2 int numbers, a and b.
#Print True if a greater Than or equal to b. if not print false
"""
Num1 = int(input("Num1: "))
Num2 = int(input("Num2: "))
if(Num1>=Num2):
    print("Num1 is greater than Num2")
else:
    print("Num2 is greater than Num2") 

#CONDITIONAL STATEMENTS
# Grade System
marks = int(input("Marks: "))

if(marks >= 90):
    grade = 'A+'
elif(marks >= 80 and marks < 90):
    grade = 'A'
elif(marks >= 70 and marks < 80):
    grade = 'B'
elif(marks >=50 and marks < 70):
    grade = 'C'
elif(marks >= 33 and marks < 50):
    grade = 'D'
else:
    grade = 'F'

print("Grade of the Student: ",grade) 

#check whether the number is even or odd 
Var1 = int(input("Num1: "))
if(Var1 % 2 == 0):
    print("The number entered by the user is an even number.")
else:
    print("The number entered by the user is an odd number.") """

#find the greatest of three numbers entered by the user.
num1 = int(input("num1: "))
num2 = int(input("num2: "))
num3 = int(input("num3: "))
if(num1 >= num2 and num1 >= num3):
    print("Number1 is the greatest number")
elif(num2 >= num3 and num2 >= num1):
    print("Number2 is the greatest number")
else:
    print("Number3 is the greatest number")

#TUTORIAL SOLUTION
num1 = int(input("num1: "))
num2 = int(input("num2: "))
num3 = int(input("num3: "))
if(num1 >= num2 and num1 >= num3):
    print("Number1 is the greatest number")
elif(num2 >= num3):
    print("Number2 is the greatest number")
else:
    print("Number3 is the greatest number")

#check if a number is multiple of 7 or not .
