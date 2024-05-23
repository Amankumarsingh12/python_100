'''
#add
def add(a,b):
    return a+b

#sub
def sub(a,b):
    return a-b

#mul
def mul(a,b):
    return a*b

def div(a,b):
    if b==0:
        return ""
    return a/b

game = False

while not game:
    a=int(input("plz enter a number: "))
    operation = input(" + \n - \n / \n * \n")

    b=int(input("plz enter a number: "))

    if operation == "+":
        print(add(a,b))
    
    elif operation == "-" :
        print(sub(a,b))

    elif operation == "*" :
        print(mul(a,b))
    
    elif operation == "/" :
        print(div(a,b))

    else :
        print("please enter valid operation")  


    game = input("yes to continue :")
    if game == "yes":
        game = False
    else:
        game = True



'''



#add
def add(a,b):
    return a+b

#sub
def sub(a,b):
    return a-b

operation ={
    "+" : add,
    "-" : sub,
}

for keys in operation :
    print(keys)

symbol = input()

print(f"{5} {symbol} {5} = {operation[symbol](5,5)}")