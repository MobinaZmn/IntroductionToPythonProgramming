def func2(Val):
    Temp = ""
    value = 0
    DotPos = 0
    for i in Val:
        if i != ".":
            Temp += i
        else:
            DotPos = Val.index(i)

    HelpValue = len(Temp) - 1
    Help = ['0','1','2','3','4','5','6','7','8','9']
    
    for x in Temp:
        value = value + (Help.index(x) * (10 ** (HelpValue)))
        HelpValue -= 1
    value = value / (10 ** (DotPos)) 
    return value
