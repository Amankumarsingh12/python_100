from coffie_machine_menu import MENU,resources

#print(MENU["espresso"]["ingredients"]["water"])
#print(resources)
#user = input("What would you like? (espresso/latte/cappuccino): ")


def money(penny,nickel,dime,quater):
    return (penny * 0.01) + (nickel * 0.05) + (dime * 0.10) + (quater * 0.25)


def coffie(user,cost):
    for key in MENU[user]["ingredients"]:
        resources[key] = resources[key] - MENU[user]["ingredients"][key]

    
    if cost - MENU[user]["cost"] > 0:
        print(f"here is your {cost - MENU[user]['cost']}") 
        print(f"Here is your {user} ☕️. Enjoy!")


user = "report"
user = "latte"
cost =0

for key in resources :
    pass
    print(key," : ",resources[key])

if user == "report" :
    for key in resources :
        pass
        print(key," : ",resources[key])

elif user == "espresso" :
    coffie(user,cost)


elif user == "latte" :
    cost = money(9,9,9,9)
    coffie(user,cost)
    pass

elif user == "cappuccino" :
    pass

else :
    print("not valid")

for key in resources :
    pass
    print(key," : ",resources[key])

