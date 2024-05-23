from random import randint

rand_num = randint(1,100)
#print(rand_num)

game = False

level = input("level of difficulty 'easy' or 'hard' ")
if level == "easy":
    attemp = 10
elif level == "hard" :
    attemp = 5
else:
    print("valid easy or hard")
    


i=0
while not game:

    num = int(input("enter a number a guess "))

    if num < rand_num :
        print("too low")
    elif num > rand_num :
        print("too high")
    else :
        print("you win")
        game = True
        break
    
    i += 1
    print(f"now only {attemp-i} left")
    if i == attemp:
        game = True
        print("you loos")
        print(rand_num)

