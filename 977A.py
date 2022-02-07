i=input().split()
i=[int(x) for x in i]
n=i[0]
k=i[1]
while k>=1:
    if(n%10==0):
        n=n//10
    else:
        n-=1
    k-=1
print(int(n))
