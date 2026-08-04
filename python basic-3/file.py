f=open("demo.text","rt")

data = f.read()

line1 = f.readline()
print(line1)
print(data)
print(type(data))
f.close()
#Over-write a data
f =open("Demo.text","w")

f.write("i want to learn python.")

f.close()
#appending a data
f =open("Demo.text","a")

f.write("hello world")

f.close()

#replace a data
new_data= data.replace("python","Java")
print(new_data)
f.close()
#replace write a data
f=open("demo.text","w")
new_data= data.replace("python","Java")
f.write(new_data)
print(new_data)

f.close()
word = "hello"
f = open("Demo.text","r")

data = f.read()

if(data.find(word) != -1):
    print("found")
else:
    print("not found")
f.close()





