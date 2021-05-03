def prog3(num):
    if num>1:
        s=int(num/2)
        for i in range(2,s+1):
            if num%i==0:
                return(False)
                break
        return(True)