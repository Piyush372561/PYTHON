print("I/O file.....")

"""f = open("sample.txt","r")
data = (f.read())
print(data)

f.close() """

with open("sample.txt","r") as f:
    data = f.read()
    print(data)

#closed file pe operation perform nhi kr rha 
with open("sample.txt","w") as f: #but yaha we opened the same file again ?
    f.write("new data")    