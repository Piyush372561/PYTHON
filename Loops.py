print("Loops in Python.")
# while loop 

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

print("Loop Ended") """

#Question --> 3 Multiplication table of a number n
n = int(input("number: "))
table = 0
i = 1
while i <= 10 :
     table += n*i
     print(table)
     i += 1
