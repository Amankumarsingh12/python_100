a=22/7
print(int(a))

height=float(input("enteryour hright "))
weight=float(input("input your weight "))

bmi=round(weight/height ** 2)

# bmi=int(bmi)
print("your bmi =" + str(bmi))

if bmi < 18.5 :
    print(f"{bmi} underweight")
elif bmi > 18.5 and bmi <25:
    print(f"{bmi} normal weight")
elif bmi > 25 and bmi <30:
    print(f"{bmi} over weight")
elif bmi > 30 and bmi <35:
    print(f"{bmi} obese")
elif bmi > 35:
    print(f"{bmi} clinical obbies")
else:
    print(f"{bmi} no")

#/ float // int

