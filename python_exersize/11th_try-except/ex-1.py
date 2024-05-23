fruits = eval(input())

def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print("index small kar")
    else:
        print(fruit + "pie")


make_pie(2)
