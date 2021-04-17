import math
'''
Calculates the area between the 4 numbers given and if the 4th number is 0 It calculates the area between the other 3
'''
def Area(A,B,C,D,E):
    if (D != 0):
        SFirst = (A + B + E) / 2
        SSecond = (E + D + C) / 2
        AreaValue = math.sqrt(SFirst * (SFirst - A) * (SFirst - B) * (SFirst - E)) + math.sqrt(SSecond * (SSecond - C) * (SSecond - D) * (SSecond - E))
    else:        
        S = (A + B + C) / 2
        AreaValue = math.sqrt(S * (S - A) * (S - B) * (S - C))
    return AreaValue
