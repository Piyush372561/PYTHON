print("I/O file.....")

f = open("demo.txt","r")#Opening a file
data = f.read()#reading number of characters
f2 = open("sample.txt","w")
f2.write("This is a new line.")
print(data)
print(type(data))


#data = f.read(5)#reading number of characters
line1 = f.readline()
print(line1)

f.close()#Closing a file