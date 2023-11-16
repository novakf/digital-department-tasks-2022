import datetime

nums=input()
start_date = datetime.datetime.strptime(nums, "%d-%m-%Y")
result_date = start_date - datetime.timedelta(days=datetime.datetime.weekday(start_date))
if result_date.day <10:
    if result_date.month <10:
        print(f'0{result_date.day}-0{result_date.month}-{result_date.year}')
    else:
        print(f'0{result_date.day}-{result_date.month}-{result_date.year}')
else:
    if result_date.month <10:
        print(f'{result_date.day}-0{result_date.month}-{result_date.year}')
    else:
        print(f'{result_date.day}-{result_date.month}-{result_date.year}')