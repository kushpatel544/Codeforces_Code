a=input().split()
n=int(a[0])
k=int(a[1])
if(n%2==0):
    o=n//2
else:
    o=(n+1)//2
if(k <= o):
    print(k*2-1)
else:
    print((k - o)*2)
