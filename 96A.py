str=input()
p1=set(str.split('1'))
p0=set(str.split('0'))
c=0
for i in p1:
    if(len(i)>=7):
        c+=1
        break
for i in p0:
    if(len(i)>=7):
        c+=1
        break
if(c>0):
    print("YES")
else:
    print("NO")

