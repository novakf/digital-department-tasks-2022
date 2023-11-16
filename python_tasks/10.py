def lists_sum(*args, unique=False):
    sum=0
    sum1=0
    uniq=[]
    for arg in args:
        for num in arg:
            sum+=num
            if num not in uniq:
                uniq.append(num)
                
    for u in uniq:
        sum1+=u
    if unique==False:
        return sum
    else:
        return sum1