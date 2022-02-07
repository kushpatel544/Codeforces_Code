a=input().split()
n=int(a[0])
m=int(a[1])
f=input().split()
f=[int(x) for x in f]
f.sort()
min=f[m-1]
for x in range(0,m-n+1):
    diff=f[x+n-1]-f[x]
    if(diff<min):
        min=diff
print(min)
