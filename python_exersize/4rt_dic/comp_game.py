'''
from comp_game_data import data

from random import randint

a = randint(0,len(data))
b = randint(0,len(data))


#print(f"A:: {data[a]['name']} , {data[a]['description']}, from{data[a]['country'}")
print(f"\n\nA:: {data[a]['name']} a {data[a]['description']}  from {data[a]['country']}")
print(f"B:: {data[b]['name']} a {data[b]['description']}  from {data[b]['country']}\n\n")


val = input("type a ,b ")

if val == "a" :
    if data[a]['follower_count'] > data[b]['follower_count'] :
        print(f"you win a={data[a]['follower_count']} b={data[b]['follower_count'] }")
    else :
        print(f"you loss a={data[a]['follower_count']} b={data[b]['follower_count'] }")

elif val == "b" :
    if data[b]['follower_count'] > data[a]['follower_count'] :
        print(f"you win a={data[b]['follower_count']} b={data[a]['follower_count'] }")
    else :
        print(f"you loss b={data[b]['follower_count']} a={data[a]['follower_count'] }")

'''

from comp_game_data import data

from random import choice

def format_data(acount):
    name = acount["name"]
    des= acount['description']
    country = acount['country']
    return f"{name}, a {des}, from {country}"


def check_ans(guess, a_follower, b_follower):
    if a_follower > b_follower:
        return guess == 'a'
    else:
        return guess == 'b'
    
score = 0

acount_a = choice(data)
acount_b = choice(data)

if acount_a == acount_b:
    acount_b = choice(data)


print(f"{format_data(acount_a)}   {acount_a['follower_count']}")

print(f"{format_data(acount_b)}    {acount_b['follower_count']}")


#guess = input("who has more follower a,b ").lower()
guess = 'a'

a_count = acount_a['follower_count']
b_count = acount_b['follower_count']
is_correct = check_ans(guess,a_count,b_count)

if is_correct :
    score += 1
    print(f"right {score}")
else:
    print(f"wrong  {score}")













