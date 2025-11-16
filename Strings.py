print("Chapter2 --> Strings")
#we can create strings in three ways:

# 1. With Single Quotes
str1 = 'String1'
print(str1)

#2. With Double Quotes
str2 = "String2"
print(str2)

#3. With Triple Quotes
str3 = """String3"""
print(str3)

#length  of a string 
print(len(str1))

#Indexing


#Slicing
str4 = "Piyush Kushwaha"
print(str4[0:len(str4)])
#negative indexing
str5 = "SRGI"
print(str5[-4:-1])

#Functions in String
S = "Hello! My name is Piyush Kushwaha"
print(S.endswith("29")) #returns true if string ends with substr

# .cpaitalise() method does not modified the string but it copies the original string and return a new string.
print(S.capitalize())

print(S.replace("Kushwaha","Malhotra"))

print(S.find("Piyush"))

print(S.count("i"))

