x = 5
y = "Jeet"
print(x)
print(y)

# casting
x = str(x)  # convert from int to str
y = int(x)  # convert from str to int
z = float(x)  # convert from str to float

print(x)
print(y)
print(z)

#type
print(type(x))
print(type(y))
print(type(z))

#assign multiple values
a, b, c = 1, 2, "Jeet"

print(a)
print(b)
print(c)

# unpack a collection
fruits = ["apple", "banana", "cherry"]

x, y, z = fruits

print(x)
print(y)
print(z)

#Global & local variables
x = "awesome"

def myfunc():
    x = "fantastic"
    print("Python is " + x + " -> Local variable")   
  
myfunc()
print("Python is " + x+" -> Global variable")

def myfunc1():
    global x
    x = "fantastic"

myfunc1()
print("Python is " + x+" -> Global variable after using global keyword")