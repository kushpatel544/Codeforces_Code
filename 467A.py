n=int(input())
f=0
for i in range(n):
    r=input().split()
    p=int(r[0])
    q=int(r[1])
    if((q-p)>=2):
        f+=1
print(f)