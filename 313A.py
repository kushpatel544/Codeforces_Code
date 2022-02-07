n=int(input())
if(n<0):
    n=abs(n)
    k=n//10
    l=n-n%100
    l=l//10+n%10
    print(max(-k,-l))
    
else:
    print(n)