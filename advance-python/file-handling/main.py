# file create
# file = open('example.txt', 'x')

# write data into the file
# file = open('example.txt', 'a/w')
# data = "a prefix appearing in loanwords from Greek, most often attached to verbs and verbal derivatives, with the meanings “at or to one side of, beside, side by side” ( parabola; paragraph; parallel; paralysis ), “beyond, past, by” ( paradox; paragogue ); by extension from these senses, this prefix came to designate objects or activities auxiliary to"
# file.write(data)

# file.close()


# file = open('example.txt', 'r')
# data = file.read()
# data = file.read(11)
# data = file.readline()
# print(data)
# data = file.readline()
# print(data)
# data = file.readline()
# print(data)
# data = file.readline()
# print(data)
# data = file.readline()
# print(data)
# data = file.readline()
# print(data)

# data = file.readlines()
# print(data)
# file.close()

# file = open('example.txt', 'w')
# lines = ['This is a line 1\n', 'This is a line 2\n', 'This is a line 3\n', 'This is a line 4\n', 'This is a line 5\n', 'This is a line 6\n']
# new_line = ['This is a new line - 7']
# lines.extend(new_line)
# file.writelines(lines)
# file.close()
# file.write("Hello")

# import uuid

# file_name = str(uuid.uuid4())
# ext = '.txt'
# # open(file_name + ext, 'w')

import os

# os.rename('example.txt', file_name + ext )

# os.remove('f1ca0702-5018-4687-aeb8-64ca02cc96d3.txt')

# os.system('mkdir test')
# os.system('rmdir test')

import os 

# os.system('py app.py')
# os.system('notepad')
# os.system('date')