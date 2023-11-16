def get_balance(name, transactions):
    sum=0
    for transaction in transactions:
        fl=0
        for keys, values in transaction.items():
            if keys=="name" and values == name:
                fl=1
            if fl==1 and type(values)==int:
                sum+=values
    return(sum)    
    
    

def count_debts(names, amount, transactions):
    dict={}
    for name in names:
        diff=get_balance(name, transactions) - amount
        if diff <0:
            dict[name]=abs(diff)
        else:
            dict[name]=0
    return dict