'''

# chr-> int to ascii     ord-> ascii to int

# generatee a number
num_list = [i for i in range(0,10)]

# generatee a char
char_list = [chr(i) for i in range(ord('a') , ord('z')+ 1    )]

# generate a special symbol
special_symbol = []
for i in "!@#$%^&*(){}[]<>" :
    special_symbol.append(i)


#ask youser how many charecter he want
length_num =   int(input("how many number "))
length_char =  int(input("how many char "))
length_special =  int(input("how many special symbol "))

import random

password = ""

#char
for i in range(0,length_char):
    password += char_list[random.randint(0,25)]

#num
for i in range(0,length_num):
    password += str(num_list[random.randint(0,9)])

#special symbol
for i in range(0,length_special):
    password += special_symbol[random.randint(0,14)]

print(password)

new_pass=random.sample(password , length_special+length_num+length_char)  

password=''
password=''.join(new_pass)
print(password)







'''
#for charecter
char_list = [chr(i) for i in range(ord('a') , ord('z')+1) ]

#for number
num_list = [i for i in range(0,9)]

#for special simpbol
special_symbol = []
for i in "!@#$%^&*(){}<>":
    special_symbol.append(i)

import random

#ramdom sample can take any five

char_len=5
num_len=5
sp_sy=5

password=''

#for char
for i in ( random.sample(char_list,char_len) ) :
    password += i

#for num
for i in ( random.sample(num_list,num_len) ):
    password += str(i)

#for special symbol
for i in ( random.sample(special_symbol,sp_sy) ):
    password += i


print(password)

password_list=[]
for i in password:
    password_list.append(i)

random.shuffle(password_list)

password=''
for i in password_list:
    password += i


print(password)

