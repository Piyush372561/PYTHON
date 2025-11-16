#List

# 1.
student = [99.5,49.5,98.6,35.9,39.05]
print(student)
print(type(student))
print(len(student))

# 2.We can also create a list of different types of elements
students = ["Arav", 41 , 21.9, True, None]
print(students) 
print(type(students))
students[0] = 'Piyush'
print(students) 
print(len(students))

# LIST SLICING
marks = [84,77,95,74,66]
print(marks[1:4])
print(marks[-3:-1])

#Add an element at the end of the list.
marks.append(51)
print(marks)

# SORTING IS ALSO POSSIBLE IN STRINGS.
#  
#list sorts in ascending order
marks.sort()
print(marks)

#List sorts in descending order.
marks.sort(reverse=True)
print(marks)

#
list = ['a', 'b', 'c', 'd', 'e']

#reverse list
list.reverse()
print(list)

#insert element at index
list.insert(1,'p')
print(list)

#this method removes first occurence of element
list.remove('a')
print(list)

#this removes element at idx
list.pop(4)
print(list)