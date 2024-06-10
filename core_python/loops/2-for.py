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


num = 6
for row in range(1,num):
    for col in range(1,num-row):
        print(' ', end=" ")
    for col in range(1,row+1):
        print('-', end=" ")
    for col in range(1,row):
        print('-', end=" ")
    print()
for row in range(1,num):
    for col in range(1,row+1):
        print(' ', end=" ")
    for col in range(1,num-row):
        print('-', end=" ")
    for col in range(1,num-1-row):
        print('-', end=" ")
    print()

