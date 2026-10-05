str = 'Hello, World!'

print(str)  

#Multiline Strings
str1 = """This is a multiline string that spans
multiple lines. It can be used to create long strings that are easier to read and maintain."""

print(str1) 

# Strings are arrays
str2 = "Hello, World!"
for i in str2:
    print(i)
    
#Length of a string
print(len(str2))

# check if a certain phrase or character is present in a string
txt = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present.")
    
#slicing Strings
b = "Hello, World!"

print(b[2:5])  # returns characters from index 2 to 5 (not included)

#slicing from the start
print(b[:5])  # returns characters from the start to index 5 (not included)

# slicing to the end
print(b[2:])  # returns characters from index 2 to the end

#Negative Indexing
print(b[-5:-2])  # returns characters from index -5 to -2 ( not included)

# String Methods
a = "  Hello, World!  "

print(a.upper())  # converts string to uppercase
print(a.lower())  # converts string to lowercase
print(a.strip())  # removes whitespace from the beginning or the end
print(a.replace("H", "J"))  # replaces a string with another string
print(a.split(","))  # splits the string into a list where each item is a substring between the commas

# String Concatenation
a = "Hello"
b = "World"
c = a + " " + b  # concatenates strings with a space in between

# String Formatting
age = 36
print("My name is John, and I am {} years old.".format(age))  # using format() method
print(f"My name is John, and I am {age} years old.")  # using f-string formatting

# String Methods
txt = "Hello, welcome to my world."
print(txt.capitalize())  # converts the first character of the string to uppercase
print(txt.title())  # converts the first character of each word to uppercase
print(txt.count("o"))  # counts the number of occurrences of a substring
print(txt.find("welcome"))  # returns the index of the first occurrence of a substring
print(txt.rfind("welcome"))  # returns the index of the last occurrence of a substring
print(txt.startswith("Hello"))  # checks if the string starts with a certain substring
print(txt.endswith("world."))  # checks if the string ends with a certain substring
print(txt.isalpha())  # checks if all characters in the string are alphabetic
print(txt.isdigit())  # checks if all characters in the string are digits
print(txt.isalnum())  # checks if all characters in the string are alphanumeric
print(txt.islower())  # checks if all characters in the string are lowercase
print(txt.isupper())  # checks if all characters in the string are uppercase
print(txt.isspace())  # checks if all characters in the string are whitespace
print(txt.swapcase())  # swaps the case of all characters in the string 
print(txt.center(50, "*"))  # centers the string and fills the remaining space with a specified character
print(txt.ljust(50, "*"))  # left-justifies the string and fills the remaining space with a specified character
print(txt.rjust(50, "*"))  # right-justifies the string and fills the remaining space with a specified character
print(txt.zfill(50))  # pads the string with zeros on the left until it reaches a specified length
