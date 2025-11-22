"""print("Recursion.....")

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

#Write a recursive function to calculate the sum of first n natural numbers.
#self written code 
def addition(n):
     sum = 0
     if(n <= 5):
       sum += n
     print(sum)

print(addition(int(input("Enter the number: "))))"""

#exact solution
def calc_sum(n):
     if(n == 0):
       return 0
     return calc_sum(n-1) + n

sum = calc_sum(5)
print(sum)

# Write a recursive function to print all elements in a list.
# Hint: use list & index as parameters

def reoccur_func(list,idx = 0):
         if(idx == len(list)):
              return
         print(list[idx])
         reoccur_func(list, idx + 1)


fruits = ["mango","litchi","apple","banana"]
reoccur_func(fruits)