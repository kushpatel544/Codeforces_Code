#URL- https://codeforces.com/problemset/problem/1475/B

n=int(input())
a=[]
for x in range(n):
    a.append(int(input()))
for x in a:
    p=x%2020
    q=x/2020
    if(p<=q):
        print("YES")
    else:
        print("NO")
        
        

