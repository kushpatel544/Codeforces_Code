
i1=input().split()
ints1 = [int(item) for item in i1]
k=ints1[0]
n=ints1[1]
w=ints1[2]
s=w*((k+w*k)/2)
if s>n:
    print(int(s-n))
else:
    print(0)
