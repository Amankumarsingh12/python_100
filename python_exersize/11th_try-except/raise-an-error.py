#raise KeyError("ak sibbfg")

height = float(input("heoght: "))
weight = int(input("weight:"))

if height > 3:
    raise ValueError("human no 3m")

bmi = weight / height ** 2
print(bmi)

