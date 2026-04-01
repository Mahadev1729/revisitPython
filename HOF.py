def add(a,b):
    return a+b

def HOF(func,a,b):
    return func(a,b)

print(HOF(add,6,7))

