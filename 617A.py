n=int(input())
i=5
c=0
while i>=0 and n!=0:
    if(n>=i):
        c+=n//i
        n=n%i
    i-=1
print(c)