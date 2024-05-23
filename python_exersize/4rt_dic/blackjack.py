import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def me():
    return random.choice(cards)

def machine():
    return random.choice(cards)


my_card = 0
machine_card = 0


machine_card =  machine() + machine_card

print(f"machine ={machine_card}")
while my_card <=21 :
    if input("hit stand ") == "hit" :
        pre_me = my_card
        my_card = my_card + me()
        print(my_card)
    else :
        pre_me = my_card
        break

while machine_card <=21 :
    pre_mac = machine_card
    if machine_card <=17 :
        machine_card =  machine() + machine_card
        print(machine_card)
    else :
        break
    
    

'''
    my_card = me(my_card)
    my.append(my_card)

    machine_card = machine(machine_card)
    you.append(machine_card)
'''

  
if pre_me > pre_mac :
    print(f"you={pre_me} mac={pre_mac}\n\n you win")

elif pre_me == pre_mac :
    print(f"you={pre_me} mac={pre_mac}\n\nDraw")

else:
    print(f"you={pre_me} mac={pre_mac}\n\n you loss")


print(my_card,machine_card)



