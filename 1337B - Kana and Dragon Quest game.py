import math

t=int(input())
for x in range(t):
    s=input().split()
    x=int(s[0])
    n=int(s[1])
    m=int(s[2])
    
    while(n):
        a=x
        v=(math.floor(x/2)+10)
        n-=1
        x=min(a,v)

    if(x-(m*10)<=0):
        print("YES")
    else:
        print("NO")