s=0
while True:
    a = input()
    if a == "":
        break
    if int(a)%2==0:
        s+=int(a)
print(s)