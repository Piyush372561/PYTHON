
# W A F to print the lenght of a list. (list is the parameter)
def print_len(list):
    print(len(list))

l = [1,2,3,4,5]
print_len(l)

# W A F to print the elements of a list in a single line.(list is the parameter)    
def print_el(list):
    for el in list:
       print(el, end = " ")
l2 = ["Piyush","daksh","Vaishnavi","Vaibhav","ARyan"]
print_el(l)
print()
print_el(l2)
print()

# W A F to print the elements of a list in a single line. (list is the parameter)
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    print(fact)
factorial(5)

#W A F to convert USD to INR.
def converter(usd_val):
    inr_val = usd_val *83
    print(usd_val, "USD =", inr_val, "INR")

converter(10)    


# ek function likho jisme ek number input hoga or agr number odd hai toh vo odd print krega or agr even huaa toh vo even print krega 
def Odd_Even(n):
    if(n % 2 != 0):
        print("Odd")
    elif(n % 2 == 0):
        print("Even")
    else:
        print("Invalid Input.")

Odd_Even(6)        

