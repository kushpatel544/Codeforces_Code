#URL - https://codeforces.com/problemset/problem/34/B

a=input().split()
n=int(a[0])
m=int(a[1])
s=input().split()
s=[int(x) for x in s]
s.sort()
sum=0
for x in range(m):
    if(s[x]<0):
        sum+=s[x]
    else:
        break
print(abs(sum))
