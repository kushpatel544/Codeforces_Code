i=input()
i=int(i)
str=""
for x in range(i):
 strx=input()
 str=str + strx
x=0
x=str.count("++")
x=x-str.count("--")
print(x)
