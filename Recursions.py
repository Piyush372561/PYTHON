print("Recursion.....")

#print the values = 5, 4, 3, 2, 1
def show(n):
    if(n == 0):
        return
    print(n)
    show(n-1)

show(5)

#factorial using Recursion
def factorial(n):
      if(n == 0 or n == 1): #correct use of or 
           return 1
      else:
           return factorial(n-1) * n
      
fact = factorial(1)
print("Factorial:",fact)

