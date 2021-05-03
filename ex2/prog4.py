Div = []
def prog4(num):
    Div.clear()
    for i in range(1,num+1):
            if(num % i == 0):
                Div.append(i)          
    return Div
