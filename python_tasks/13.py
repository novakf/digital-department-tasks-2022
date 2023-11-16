def get_popular_name_from_file(filename):
    f = open(filename, mode = 'r')
    names = {}
    res=[]
    for line in f:
        name = line.split(" ")[0]
        names[name]=0
    
    f.seek(0)
    for line in f:
        name = line.split(" ")[0]
        names[name]+=1
    k=0
    max_val = max(names.values())

    for keys, values in names.items():
        if values == max_val:
            res.append(keys)
            k+=1
        
    res = sorted(res)
    s=""
    n=0
    for name in res:
        n+=1
        if k==1 or (n==k and k!=1):
            s+=name
        else:
            s+=name+ ", "
    return s