# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5

num = 6
for row in range(1,num):
    for col in range(1,num):
        print(col, end=" ")
    print()


# A B C D E
# A B C D E
# A B C D E
# A B C D E
# A B C D E

num = 6
for row in range(1,num):
    for col in range(1,num):
        print(chr(col + 64), end=" ")
    print()

# a b c d e
# a b c d e
# a b c d e
# a b c d e
# a b c d e

num = 6
for row in range(1,num):
    for col in range(1,num):
        print(chr(col + 96), end=" ")
    print()

# 1 1 1 1 1
# 0 0 0 0 0
# 1 1 1 1 1
# 0 0 0 0 0
# 1 1 1 1 1

num = 6
for row in range(1,num):
    for col in range(1,num):
        if row % 2 != 0:
            print("1", end=" ")
        else:
            print("0", end=" ")
    print()


# 1 0 0 0 0
# 0 1 0 0 0
# 0 0 1 0 0
# 0 0 0 1 0
# 0 0 0 0 1

num = 6
for row in range(1,num):
    for col in range(1,num):
        if row == col:
            print("1", end=" ")
        else:
            print("0", end=" ")
    print()


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

num = 6
for row in range(1,num):
    for col in range(1,num):
        if row == 1 or col == 1 or row == num - 1 or col == num-1:
            print("1", end=" ")
        else:
            print(" ", end=" ")
    print()

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

num = 6
for row in range(1,num):
    for col in range(1,row+1):
        print(col, end=" ")
    print()

# - - - - -
#   - - - -
#     - - -
#       - -
#         -

num = 6
for row in range(1,num):
    for col in range(1,row):
        print(' ', end=" ")
    for col in range(1,num+1-row):
        print('-', end=" ")
    print()

#         *
#       * *
#     * * *
#   * * * *
# * * * * *

num = 6
for row in range(1,num):
    for col in range(1,num-row):
        print(' ', end=" ")
    for col in range(1,row+1):
        print('*', end=" ")
    print()

#         *
#       * * *
#     * * * * *
#   * * * * * * *
# * * * * * * * * *

num = 6
for row in range(1,num):
    for col in range(1,num-row):
        print(' ', end=" ")
    for col in range(1,row+1):
        print('*', end=" ")
    for col in range(1,row):
        print('*', end=" ")
    print()

# - - - - - - - - -
#   - - - - - - -
#     - - - - -
#       - - -
#         -
num = 6
for row in range(1,num):
    for col in range(1,row):
        print(' ', end=" ")
    for col in range(1,num+1-row):
        print('-', end=" ")
    for col in range(1,num-row):
        print('-', end=" ")
    print()


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


# 1 2 3 4 5
# 6 7 8 9 10
# 11 12 13 14 15
# 16 17 18 19 20
# 21 22 23 24 25

num = 5
global_var = 1
for row in range(1, num+1):
    for col in range(1, num+1):
        print(global_var, end=' ')
        global_var+=1
    print()


# 1 2 3 4
# 5 6 7
# 8 9
# 10

num = 5
global_var = 1
for row in range(1, num+1):
    for col in range(1, num+1-row):
        print(global_var, end=' ')
        global_var+=1
    print()


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