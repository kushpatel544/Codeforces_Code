n=int(input())
a=input().split()
a=[int(x) for x in a]
sum=0
ans=0
c=0
for x in a:
    sum+=x
sum//=2
a.sort(reverse=True)
for x in a:
    ans+=x
    c+=1
    if(ans>sum):
        break
print(c)