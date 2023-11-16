import datetime, math

dates=[]

def gift_count(budget, month, birthdays):
    for value in birthdays.values():
        dates.append(value)
    
    birthdays = dict(sorted(birthdays.items(), key=lambda item: item[1].day))
    
    num=0  
    for keys, result_date in birthdays.items():
        if result_date.month==month:
            num+=1

    if num!=0:        
        print(f'Именинники в месяце {month}: ', end='')
    else:
        print("В этом месяце нет именинников.")
    i=0
    
    for keys, result_date in birthdays.items():
        if result_date.month==month:
            i+=1
            print(keys, end=' ')
            if result_date.day <10:
                if result_date.month <10:
                    print(f'(0{result_date.day}.0{result_date.month}.{result_date.year})', end='')
                    if i!=num:
                        print(', ', end='')
                else:
                    print(f'(0{result_date.day}.{result_date.month}.{result_date.year})', end='')
                    if i!=num:
                        print(', ', end='')
            else:
                if result_date.month <10:
                    print(f'({result_date.day}.0{result_date.month}.{result_date.year})', end='')
                    if i!=num:
                        print(', ', end='')
                else:
                    print(f'({result_date.day}.{result_date.month}.{result_date.year})', end='')
                    if i!=num:
                        print(', ', end='')
    if num!=0:
	    print(f'. При бюджете {budget} они получат по {math.floor(budget/num)} рублей.')