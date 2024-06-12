"""
String : immutable
A string is a fundamental data type in Python, and most programming languages, representing a sequence of characters. Here's a detailed explanation of what a string is and how it works in Python:

Definition:

A string is a sequence of characters enclosed within single quotes ('...'), double quotes ("..."), triple single quotes ('''...'''), or triple double quotes (\"\"\"...\"\"\").
For example: "Hello, World!", 'Python', '''This is a multi-line string''', and \"\"\"Another multi-line string\"\"\".

Immutability:

Strings in Python are immutable, which means once a string is created, it cannot be changed. Any operation that modifies a string will create a new string.

"""

code = "python"

# print(type(code)) # <class 'str'>
# print(len(code)) # 6

# indeing (+/-):  Accessing individual characters in a string using zero-based indices.

# left to right(+)
# print(code[0])
# print(code[1])

# for ch in range(len(code)):
#     print(code[ch])

# right to left(-)
# print(code[-1])
# print(code[-2])

# for ch in range(len(code)-1, -1, -1):
#     print(code[ch])

# slicing : Extracting a substring using a range of indices.

# left to right(+)
# print(code[2:5])
# print(code[2:5])

# concatination : Joining two or more strings together using the + operator.
# print(code[:2] + code[len(code)-1:])

str1 = "Hello"
str2 = "World"
result = str1 + " " + str2  # "Hello World"


# right to left(-)
# print(code[::-1])
# print(code[-1:-5:-1])

# Repetition: Repeating a string multiple times using the * operator.
# print("*"*5)

# *
# **
# ***
# ****
# *****
# num = 6
# for row in range(1,num):
#     print("*"*row)

# *****
# ****
# ***
# **
# *
# num = 6
# for row in range(1,num):
#     print("*"*(num-row))

#   *****
#    ****
#     ***
#      **
#       *

# num = 6
# for row in range(1,num):
#     print(" "*(row), "*"*(num-row))

#    * * * * *
#     * * * *
#      * * *
#       * *
#        *

# num = 6
# for row in range(1,num):
#     print(" "*(row), " *"*(num-row))

# print(dir(code))

# String methods: 

name = "ToPS TecHnoLOgy PvT. LTd."

# print(name.lower())
# print(name.upper())
# print(name.title())
# print(name.capitalize())
# print(name.swapcase())

# star = "*"
# print(star.center(5, '-'))

# print(name.lower().find('tech'))

# print('TecH' in name)

password = "Test"
# password = "124543tjhgjuj@@$%$%"
# password = "@@$%$%"

# print(password.isalpha())
# print(not password.isalpha())
# print(password.isdigit())
# print(password.isalnum())
# print(not password.isalnum())

# print(password.startswith('Te'))
# print(password.endswith('st'))

test = "    hi helo    "
# print(len(test))
# print(test.rstrip())
# print(test.lstrip())
# print(len(test.strip()))
# print(test.replace(" ", ""))
# print(" ".join(["Hello", "World"]))


name = "python"
price = 675.34275642
page = 400

# print("book name is python and book price is 675.34275642 and total page is 400")
# f-strings (formatted string literals, introduced in Python 3.6):
# print(f"book name is {name} and book price is {price} and total page is {page}")
# print("book name is {} and book price is {} and total page is {}".format(name, price, page))
# print("book name is {2} and book price is {1} and total page is {0}".format(name, price, page))
# print("book name is %s and book price is %.2f and total page is %d" % (name, price, page))

# Unicode and Encoding:
unicode_str = "こんにちは"
encoded_str = unicode_str.encode('utf-8')  # Encode to bytes
# print(encoded_str)
decoded_str = encoded_str.decode('utf-8')  # Decode back to string
print(decoded_str)