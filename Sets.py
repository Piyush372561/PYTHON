print("Sets in python.")
num1 = {2,4,6,8,10,2,4,"hello world", "Ganesh"}
num2 = {2,4,6,8,10,2,4,"RadhaKrishna", "Mahesh"}
print(num1)
print(type(num1))
print(len(num1))

#in order to create an empty set
num3 = set()#this is a set
print(type(num2))
num4 = {} #this is a dictionary
print(type(num3))

#methods in set
print(num1.add(5))
print(num1)

print(num1.remove(5))
print(num1)

print(num1.clear())
print(num1)

print(num1.union(num2))
print(num1.intersection(num2))