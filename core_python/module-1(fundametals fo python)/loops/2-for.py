"""
For
A for loop is another control flow statement that is used to iterate over a sequence (such as a list, tuple, string, or range) or any iterable object.

syntax: 

for var/element in sequence:
    block of code
"""

# code = "python"

# for ch in code:
#     print(ch)

# for num in range(1,11):
#     print(num * num * num)

# row 
# num = 6
# for row in range(1,num):
#     print(row)

# column
# num = 6
# for col in range(1,num):
#     print(col, end=" ")


# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5

# num = 6
# for row in range(1,num):
#     for col in range(1,num):
#         print(col, end=" ")
#     print()

# A B C D E
# A B C D E
# A B C D E
# A B C D E
# A B C D E

# a b c d e
# a b c d e
# a b c d e
# a b c d e
# a b c d e

# 1 1 1 1 1
# 0 0 0 0 0
# 1 1 1 1 1
# 0 0 0 0 0
# 1 1 1 1 1

# 1 0 0 0 0
# 0 1 0 0 0
# 0 0 1 0 0
# 0 0 0 1 0
# 0 0 0 0 1

# 1 1 1 1 1
# 1 0 0 0 1
# 1 0 0 0 1
# 1 0 0 0 1
# 1 1 1 1 1

# 1 1 1 1 1
# 1       1
# 1       1
# 1       1
# 1 1 1 1 1

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

# num = 6
# for row in range(1,num):
#     for col in range(1,num+1-row):
#         print('-', end=" ")
#     print()

# - - - - -
#   - - - -
#     - - -
#       - -
#         -

#         *
#       * *
#     * * *
#   * * * *
# * * * * *

#         *
#       * * *
#     * * * * *
#   * * * * * * *
# * * * * * * * * *


# - - - - - - - - -
#   - - - - - - -
#     - - - - -
#       - - -
#         -

#         -
#       - - -
#     - - - - -
#   - - - - - - -
# - - - - - - - - -
#   - - - - - - -
#     - - - - -
#       - - -
#         -


# num = 6
# for row in range(1,num):
#     for col in range(1,num-row):
#         print(' ', end=" ")
#     for col in range(1,row+1):
#         print('-', end=" ")
#     for col in range(1,row):
#         print('-', end=" ")
#     print()
# for row in range(1,num):
#     for col in range(1,row+1):
#         print(' ', end=" ")
#     for col in range(1,num-row):
#         print('-', end=" ")
#     for col in range(1,num-1-row):
#         print('-', end=" ")
#     print()

# 1 2 3 4 5
# 6 7 8 9 10
# 11 12 13 14 15
# 16 17 18 19 20
# 21 22 23 24 25

# num = 5
# global_var = 1
# for row in range(1, num+1):
#     for col in range(1, num+1):
#         print(global_var, end=' ')
#         global_var+=1
#     print()

# 1
# 23
# 456
# 78910

# A
# BC
# DEF


# A B C D
# E F G
# H I
# J

num = 5
global_var = 1
for row in range(1, num+1):
    for col in range(1, num+1-row):
        print(chr(global_var + 64), end=' ')
        global_var+=1
    print()