x=input().split("+")
x.sort()
str=""
for i in range(0,len(x)-1):
    str=str+x[i]+"+"
str=str+x[len(x)-1]
print(str)
    
