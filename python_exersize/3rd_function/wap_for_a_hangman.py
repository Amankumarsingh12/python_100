from hangMan import word_list

#randmonllay chosseing a work from a list
import random

word_random = random.choice(word_list)



word_output = []

for word in word_random:
    word_output += "_"

print(word_random)
print(word_output)

game = False

while not game:
    char_guess = input("enter your guess charector ").lower()
    for position in range(len(word_output)):
        letter = word_random[position]
        if letter == char_guess:
            word_output[position] = letter

    print(word_output)

    if "_" not in word_output:
        game = True




'''
word_list = ["ardvark", "baboon", "camel"]


#randomally chossing a word
import random
word_random = random.choice(word_list)

word_output = []

for word in word_random :
    word_output += "_"


print(word_random)
print(word_output)

i = 0
while ( i+1 <= len(word_output) ):
    char_guess = input("enter your guess charector ").lower()

    if word_random[i] == char_guess[0]:
        word_output[i] = char_guess[0]
        i += 1

    print(word_output)
    
    
'''























