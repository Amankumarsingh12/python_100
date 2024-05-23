sum=0

for nu in range(0,101,2):
    sum += nu

print(sum)


my_list=input("enter your list ").split()


for value in range(0,2):
    my_list[value] = int(my_list[value])
    print(f"{value}  {type(value)}")

print(my_list)