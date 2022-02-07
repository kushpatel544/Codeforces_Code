p=[]
for x in range(5):
    str=input().split()
    str=[int(item) for item in str]
    p=p+[str]

def fun(i,j):
    print(abs(i-3)+abs(j-3))
        
    

for i in range(5):
    for j in range(5):
        if p[i][j]==1:
            fun(i+1,j+1)




