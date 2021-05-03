Numbers = []
def prog2(x,y):
    Numbers.clear()
    if y < x:
        y = y + 1
        for i in range(y,x):
            if(i % 2 == 0):
                Numbers.append(i)
    else:
        x = x + 1
        for i in range(x,y):
            if(i % 2 == 0):
                Numbers.append(i)
    return Numbers