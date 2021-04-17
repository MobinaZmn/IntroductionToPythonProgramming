import math
'''
Solves the 2d equation and gives us the result
'''
def equation2D(a,b,c):
    Delta = pow(b,2) - (4*a*c)
    if(Delta > 0):
        return (-b - math.sqrt(Delta)) / (2*a), (-b + math.sqrt(Delta)) / (2*a)
    elif(Delta == 0):
        Result = (-b) / (2*a)
        return "The equation gives one result: {Res}".format(Res = Result) 
    else:
        return "Can't solve this equation"