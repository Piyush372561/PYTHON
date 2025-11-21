print("Loops in Python.")

# while loop --> jaise hume agar kisi iterator ke upar kaam krna hai jaise ki kisi variable ki value ko update krna hai fir koii stoping condition hai vo saare kaam while loop se krenge 
# Question --> 1
"""i = 1
while i <= 100 :
    print(i)
    i += 1

print("Loop Ended")

# Question --> 2
i = 100
while i >= 1 :
    print(i)
    i -= 1

print("Loop Ended") 

#Question --> 3 Multiplication table of a number n
n = int(input("number: "))
i = 1
while i <= 10 :
     print(n*i)
     i += 1 

#Question 4 = print the elements of the following list using a loop: 
# [1,4,9,16,25,36,49,64,81,100]

#ye nayi values generate kr rha hai
i = 1
while i <= 10 :
     print(i*i)
     i += 1 

#
list = [1,4,9,16,25,36,49,64,81,100]

#idx = 0
#while idx < len(list) :
 #    print(list[idx])
  #   idx += 1

#Question 5 = 
idx = 0
x = int(input("x: "))
while idx < len(list) :
     if (list[idx] == x):
          print("found at index: ", idx)
          break
     else:
          print("Finding.......")
     idx += 1

#CONTINUE
i = 0
while i <= 5 :
     if(i == 3):
          i += 1
          continue
     print(i)
     i += 1 
# printing odd numbers
n = 1
while n <= 10 :
     if(n % 2 != 0):
          n += 1
          continue #skip 
     print(n)
     n += 1 """


#FOR LOOP  --> agar hume kisi data type ke upar traverse krna hai toh vo saare kaam hum for loop se karenge
num = [2,4,6,8,10]

for val in num:
     print(val)

str = "Piyush Kushwaha"

for char in str:
     print(char)