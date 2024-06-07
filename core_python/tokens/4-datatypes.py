
# # numeric datatypes
# x = 10
# print(type(x)) # <class 'int'>

# F = 20.3465
# print(type(F))

# # string datatype
# name = "python"
# print(type(name)) # <class 'str'>

# # data-collectyion 
# items = ['pen', 'book', 'totmato', 6753, 476.6735]
# print(type(items)) # list

# nums = (1,2,3,4,5,6)
# print(type(nums)) # tuple

# numbers = {1,2,3}
# print(type(numbers)) # set

# products = {
#     'tomato':20,
#     'potato':35
# }
# print(type(products))


# implicit type conversion

x = 10
y = 10.4
y = "100"
# z = x + y # TypeError: unsupported operand type(s) for +: 'int' and 'str'
# print(type(z))

# Explicit type convesion
num = input("Enter a number : ")
f = float(num) # ValueError: could not convert string to float: 'ajhgjdfgujhdy'
i = int(f)
print(i)
print(type(i))

