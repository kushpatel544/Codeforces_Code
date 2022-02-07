i1=input().split()
i2=input().split()
ints1 = [int(item) for item in i1]
n=ints1[0]
k=ints1[1]
ints2 = [int(item) for item in i2]
place=ints2[k-1]
#print(place)
ans=[x for x in ints2 if x>=place and x!=0]
print(len(ans))