str = input()
str=str.lower()

list = sorted(str.split(', '))

i=0
while i<len(list):
    if list[i] in list[:i]:
        list.pop(i)
    else:    
        i+=1
    
res=""
for i in range(len(list)):
    res+=list[i]
    if i!=len(list)-1:
        res+=", "
        
print(res)