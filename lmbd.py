a=lambda x,y,z:z-x
print(a(10,20,30))

def fun(y):
    return lambda y:y*y
fun2=fun(0)
print(fun2(40))