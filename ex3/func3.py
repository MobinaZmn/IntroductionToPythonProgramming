def func3(s):
    i = 1
    while s > i:
        i = i * 10
    Val = 0
    while s > 1:
        while s > i:            
            s -= i
            Val += i
        i = i // 10
    return Val
