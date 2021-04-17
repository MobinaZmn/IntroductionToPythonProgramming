import random
'''
Returns an even value between the two numbers
'''
def Rand2(x,y):
    x= x + 1
    Rand = random.randint(int(x),int(y))
    while Rand % 2 != 0:
        Rand = random.randint(int(x),int(y))
    return Rand