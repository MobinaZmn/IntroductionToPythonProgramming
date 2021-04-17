import math
'''
Calculates the area between the 4 numbers given and if a number is 0 It calculates the area between the other 3
'''
def AreaX(A,B,C,D,E):
    if (A or B or C or D == 0):        
        if (D == 0):
            P1 = A
            P2 = B
            P3 = C
            S = (P1 + P2 + P3) / 2
        elif (A == 0):
            P1 = D
            P2 = B
            P3 = C
            S = (P1 + P2 + P3) / 2
        elif (B == 0):
            P1 = D
            P2 = A
            P3 = C
            S = (P1 + P2 + P3) / 2
        elif (C == 0):
            P1 = D
            P2 = A
            P3 = B
            S = (P1 + P2 + P3) / 2

        AreaValue = math.sqrt([S * (S - P1) * (S - P2) * (S - P3)])

    else:
        SFirst = (A + B + E) / 2
        SSecond = (E + D + C) / 2
        AreaValue = math.sqrt(SFirst * (SFirst - A) * (SFirst - B) * (SFirst - E)) + math.sqrt(SSecond * (SSecond - C) * (SSecond - D) * (SSecond - E))

    return AreaValue
