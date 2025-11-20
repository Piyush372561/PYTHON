print("Python Dictionaries.")
print("Here is my first Custom Dictionaries.")

# D1 --> keys me hum dictionary or list ko use nhi kr skte but value hum kisi bhi data type ki rakh skte hai, tuple ko hum key bana skte hai.
Student1 = {

    "Name":"Abhilash",
    #list
    "subjects": ["java","python","c++","c"],
    #tuples
    "topics": ("dict","sets"),
    "Roll_no":"24",
    "Seat_no.":"245",
    "Batch":"A2",

#Nested-Dictionary
    "studentsfriend": {
       "Name":"Amar",
       "Roll_no.":"29",
       "Batch":"A1",
       "Seat_no.":"230"
    }
}
print(Student1)
print(type(Student1))
Student1["Name"] = "Piyush kushwaha"
print(Student1["Name"])

#Methods_of_Dictionaries
print(Student1.keys())#returns all keys 
print(Student1.values())#returns all values
print(Student1.items())#returns the key value pairs
print(Student1.get("Name"))#
print(Student1.update({"city":"Jhansi", "State": "UP"}))#update your dictionary

#null dictionary
null_dict = {}
null_dict["Name"] = "Daksh Yadav"
print(null_dict)
#we can typecast our dictionary
print(list(null_dict))
#total number of key value pairs
print(len(list(Student1.keys())))
