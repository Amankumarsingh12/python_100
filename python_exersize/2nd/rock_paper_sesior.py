rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game=[rock,paper,scissors]

import random

rand_nu=random.randint(0,2)

your_choise=int(input("enter your choise 0->rock 1->paper 2->scissors "))

#0->rock 1->paper 2->scissors

#result=" "
if your_choise == rand_nu :
    result="Tiee"

#rock
elif your_choise == 0 and rand_nu == 1 :
    result="loss"
elif your_choise == 0 and rand_nu == 2 :
    result="win"

#paper
elif your_choise ==1 and rand_nu ==0 :
    result="win"
elif your_choise ==1 and rand_nu ==2 :
    result="loss"

#scissors
elif your_choise ==2 and rand_nu ==0 :
    result="loss"
elif your_choise ==2 and rand_nu ==1 :
    result="win"

else:
    print("enter valisd")

str_value=["rock", "paper", "scissors"]
message=f"you {str_value[your_choise]}   comp {str_value[rand_nu]}"


your_choise=game[your_choise]
comp_choise=game[rand_nu]


print("your choise\n",your_choise)
print("comp choise\n",comp_choise)

print("\n\nyou "+ result)
print(message)




