# class car:
#     # data member
#     wheels = 4
#     engine = True
#     seats = 5
#     name = "BMW"

#     # member function
#     def __init__(self):
#         print("init method called")

#     def break_(self):
#         print("car is breaking")

# class ATM:
#     def __init__(self, card_number, pin_number):
#         self.card_number = card_number # public var
#         self.__pin_number = pin_number # private var

#     def display(self):
#         print("card number is", self.card_number)
#         print("pin number is", self.__pin_number)

# brijesh = ATM("423455776357652", '1111')
# rohit = ATM("76532567574637", '1234')

# # brijesh.display()

# # rohit.display()

# # print(brijesh.__pin_number)
# print(brijesh._ATM__pin_number) # name mangling system : _className__varName