'''
def fun1(): 
    print("hello") 

def fun2(func): 
    func() 

fun2(fun1) 
'''

def fun1(msg):
    print(msg)

def fun2(fun, msg):
    fun(msg)

fun2(fun1, "hello")
