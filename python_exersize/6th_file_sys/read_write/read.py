path = "D:\\python\\file_sys\\read_write\\data.txt"
# file = open("D:\\python\\file_sys\\read_write\\data.txt")
# content = file.read()
# print(content)
# file.close()

'''
## open a file####

with open("D:\\python\\file_sys\\read_write\\data.txt") as file:
    content = file.read()
    print(content)

'''
###########################################################################################

'''
#write a file

with open(path, mode="a") as file:
    file.write("\nhii aman")
'''

#########################################################################################

#creat a file

with open("new_txt.txt", mode="w") as file:
    file.write("ho gya")