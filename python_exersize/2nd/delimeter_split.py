#wap splite a bill in three people

import random

people=input("enter the name using comma\n")

people=people.split(",")

length=len(people)

rand_nu=random.randint(0,length-1)

print(people[rand_nu])
