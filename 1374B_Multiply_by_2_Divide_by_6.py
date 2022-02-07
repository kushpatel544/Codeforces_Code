
from cmath import inf


n=int(input())
a=[]
for x in range(n):
    a.append(int(input()))

for x in a:
    n=x
    c=0
    while(n%6==0):
        n=n/6
        c+=1
    while(n%3==0):
        n=n/3
        c+=2
    if(n==1):
        print(c)
    else:
        print("-1")
    
