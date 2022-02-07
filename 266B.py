k=input().split()
n=int(k[0])
t=int(k[1])
str=list(input())
while(t):
    i=1
    while(i<len(str)):
        if str[i-1]=="B" and str[i]=="G":
            str[i-1]="G"
            str[i]="B"
            i+=1
        i+=1
    t-=1
nstr=""
for i in range(len(str)):
    nstr+=str[i]
print(nstr)


