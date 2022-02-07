p=input()
q=input()
sum=""
for i in range(len(p)):
    if(p[i]=='1' and q[i]=='1'):
        sum+='0'
    elif(p[i]=='1' or q[i]=='1'):
        sum+='1'
    else:
        sum+='0'
print(sum)