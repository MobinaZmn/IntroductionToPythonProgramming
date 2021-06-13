def func4(x):
    NewList = []
    for a in x:   
        TempTup = a
        while TempTup[1] != 0:
            TempTup = (TempTup[1], TempTup[0] % TempTup[1])      
        NewList.append((a[0]/ TempTup[0], a[1]/ TempTup[0]))
    return NewList
 
