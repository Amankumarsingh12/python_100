def prime_check(nu):
    if nu == 1:
        return "1 is a prime number"

    for n in range(2,nu):
        if not nu % n :
            return ""
            #return f"{nu} is not a prime number"
            #return nu
    
    #return f"{nu} is a prime number"
    return nu
    

for n in range(0,51):
    nu = prime_check(n)
    print(nu)

#print(prime_check(3))


            

