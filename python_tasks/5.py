i=0
s=[]

while i!=5:
    a = input()
    a=int(a)
    s.append(a)
    i+=1
    
s2=sorted(s, reverse=True)

for num in s2:
    print(num)