n=int(input())
str=input().split()
k=[int(x) for x in str]
sum=0
for i in k:
    sum+=i
print(sum/n)