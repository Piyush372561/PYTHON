print("Practice set 5.")

#Question 1
"""for num in range(1,101):
    print(num)

#Question 2
for num in range(100,0, -1):
    print(num)

#Question 3
n1 = int(input("Enter the number: "))
for el in range(1,11):
     print(n1*el) """

#q
n = 5
sum = 0
i = 1
while i <= n:
    sum += i
    i += 1

print(sum)

"""for i in range(1,n+1):
    sum += i
    print(sum) """

#Q 
n = 5
fact = 1
i = 1
while i <= n:
    fact *= i
    i += 1

print("factorial =", fact)
