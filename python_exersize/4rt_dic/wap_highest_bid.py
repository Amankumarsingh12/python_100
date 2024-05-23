
bids = {}


game=False

big =0


while not game:

    name =input("enter your name ")
    value =int(input("enter your value "))

    bids[name] = value

    game = input("exits yes,no  ")

    if value >= big:
        big =value
        winner = name

    game= game.lower() == "yes"



print(bids)
print(winner,big)

