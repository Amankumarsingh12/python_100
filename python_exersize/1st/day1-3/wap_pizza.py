size=input("size of pizza s,m,l ")
pepperoni=input("want pepperoni y,n ")
cheese=input("want cheese y,n ")

if size=="s":
    p=15
    if pepperoni=='y':
        p +=2
    if cheese=='y':
        p+=1
elif size=="m":
    p=20
    if pepperoni=='y':
        p +=3
    if cheese=='y':
        p+=1
elif size=="l":
    p=25
    if pepperoni=='y':
        p +=3
    if cheese=='y':
        p +=1
else:
    print("you enter wrong")

print(f"your pizza is {size} price is {p}")

