#Example
# function definition
def Calculator(a,b):#parameter
    sum = a + b
    print(sum)
    
    diff =  a - b
    print(diff)
    
    multi = a * b
    print(multi)

    div = a /b
    print(div)
    
 
Result = Calculator(10,12) #Functioncall; Arguments
print(Result)

#Example-2
def print_Greetings():
    print("Hello!")
    print("Good Morning")

#jo function kuch bhi return nhi krta usme none value print ho jati hai 
output = print_Greetings()
print(output)  

#average marks
def Average(a,b,c):
    total = a+b+c
    average = total/3
    print("Average od Student: ",average)

Average(45,55,50)

#ONE THE MOST IMP THINGS
print("PiyushK", end= "._.")
print("DakshY")


# non-default values should come first always
def calci(a, b = 2):
    print(a*b)
    return a * b

calci(5)