n=int(input())

a=[]
for x in range(1,n+1):
    a.append(int(input()))
for y in range(n):
    k=2
    while(True):
        x=(a[y]*(1-2))/(1-2**k)
        x=float(x)
        if(x.is_integer()):
            print(int(x))
            break
        k+=1
        
        


