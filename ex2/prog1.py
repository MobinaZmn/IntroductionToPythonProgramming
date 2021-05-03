Numbers = []
def prog1(x,y):
    Numbers.clear()
    for x in range(x+1,y):
        if(x % 2 == 0):
            Numbers.append(x)
    return Numbers