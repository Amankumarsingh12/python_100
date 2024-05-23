'''
number = [1, 2, 3]
new_list = []

for n in number:
    n = n+1
    new_list.append(n)

print(new_list)
'''
#and bellow are same
#new_list = [n+1 for n in number]



'''
name = "Angela"
new_list = [letter for letter in name]
print(new_list)
'''

#use range
# new_list = [n*2 for n in range(1, 5)]
# print(new_list)

# name = ["abcd", "efghuiij", "1234", "qwerty_ghj", "mnop"]
# #short_list = [n for n in name if len(n) <= 4]
# short_list = [n.upper() for n in name if len(n) > 4]
# print(short_list)

########challenge#######
# number = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# squared_number = [n*n for n in number]
# print(squared_number)

###chalenge 2####
# number = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# result = [n for n in number if not n%2 ]
# print(result)

###chalenge 3 #####
