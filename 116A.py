i=int(input())
ins=0
max=0
for x in range(i):
    j=input().split()
    y=[int(b) for b in j]
    a=y[0]
    b=y[1]
    ins-=a
    ins+=b
    if(ins>max):
        max=ins
print(max)

