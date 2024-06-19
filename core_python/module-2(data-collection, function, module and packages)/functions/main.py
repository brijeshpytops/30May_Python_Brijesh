"""
A function is a block of organized, reusable code that is used to perform a single, related action. Functions provide better modularity for your application and a high degree of code reusing. They allow you to break down your program into smaller and more manageable parts.

syntax: 

def function_name(para1, para2,....paran): # function defination
    # block of code

function_name(value1, value2,....valuen) # function call

inbuilt-function : print, len, type, id, sum, min, max...
user-define function : 
"""

# 100 * 4 = 400 - 102 = 298

# a = 10
# b = 20
# c = a + b
# print(c)
# d = 30 
# e = 40
# f = d + e
# print(f)

# def len(num1, num2):
#     print(num1 + num2)

# # # add(10, 20)
# # # add(30, 40)
# # len(20, 40)

# # print(sum([1,2,3,4,5,67,7]))

# l = [1,2,3,4,5,67,7]
# print(len(l))

# Type of paras

# 1] postional args
# def add(a, b):
#     print(a + b)

# add(10, 20, 30)

# def add(a, b, c):
#     print(a + b)

# add(10, 20)

# keywords/default args

# def bill(tomato=90, potato=30):
#     print(tomato+potato)

# bill(potato=50)

# varibale length args
# *args
# **kwargs

# def add(*nums):
#     # print(type(nums))
#     print(sum(nums))

# add(1,2,3,5,6,7,8,9,100)

# def bill(**products):
#     # print(type(products))
#     total_amount = 0
#     for key, value in products.items():
#         total_amount += value
#         print(key, value)
#     print("Total Amount : ", total_amount)
# bill(tomato=90, potato=30, onion=30, milk=33)

# products = {
#     'tomato':{
#         'price': 90,
#         'quantity': 2,
#     },
#     'potato':{
#         'price': 30,
#         'quantity': 3,
#     }
# }

# total_amount = 0
# for key, value in products.items():
#     print(key, value)
#     total_amount += value['price'] * value['quantity']
# print(total_amount)

# power = lambda x,y: x ** y
# print(power(2,5))

# nums = [1,2,3,4,5]
# print(list(map(lambda x: x ** 2, nums)))

# x = 20

# def test():
#     global x
#     x = 10
#     print(x)

# test()
# print(x)

# len()