"""
List - mutable, ordered, duplicate values are allowed, indexing, slicing

syntax: 

list_var = []
list_name = list()
"""

nums = [1,2,3,4,5]

# print(type(nums))
# print(len(nums))

# indexing(+/-)
# print(nums[0])
# print(nums[3])

# print(nums[-1])

# slicing
# print(nums[1:4])
# print(nums[::2])
# print(nums[::-2])

# mix_list = [12, 34.5556, "python", 'd', 'd' ,23 + 54j]
# print(mix_list)

nested_list = [1,2,[4,5, [6,7, [8,9, [11,12,[34]]]]]]
# print(nested_list[-1][-1][-1][-1][-1][-1])

sn = [1,2,3]
# print(sn*5)
dn = [11,22,33]
tn = [111,222,333]
mixn = sn + dn + tn
# print(mixn)

# for num in mixn:
#     print(num)

m_items = ['milk', 'pen']
a_items = ['tomato', 'potato']
my_items = ['drinks', 'drinks', 'drinks', 'chocolate']

mix_items = m_items + a_items + my_items

# print(mix_items)
# print(dir(mix_items))
# '', '', 'copy', '', '', '', '', '', '', '', ''
# print(len(mix_items))

s_list = my_items 

# add
# mix_items.append(s_list)
# mix_items.extend(s_list)
# mix_items.insert(0, s_list)

# update
# mix_items[4] = 'maggi'

# delete
# del mix_items[2]
# mix_items.clear()
# mix_items.pop()
# mix_items.remove('potato')
# print(mix_items.index('potato'))
# print(mix_items.count('drinks'))
# mix_items.sort()

# print(id(mix_items))
# new_list = mix_items.copy()
# print(id(new_list))

# x = 10
# print(id(x))
# y = 10
# print(id(y))