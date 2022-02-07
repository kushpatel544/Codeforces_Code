n=int(input())
a=input().split()
a=[int(x) for x in a]
max=0
c=1
for x in range(1,n):
    
    if(a[x]>=a[x-1]):
        c+=1
        if(max<c):
            max=c
      
    else:
        c=1
    
if(max!=0):
    print(max)
else:
    print(c)

