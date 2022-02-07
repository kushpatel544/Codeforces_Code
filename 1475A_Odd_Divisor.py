
n=int(input())
a=[]
for x in range(n):
    a.append(int(input()))

for x in a:
    while x!=1:
        if(x%2==0):
            x/=2
        else:
            break
    if(x==1):
        print("NO")
    else:
        print("YES")
        

