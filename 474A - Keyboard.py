#URL: https://codeforces.com/problemset/problem/474/A

dir=input()
seq=input()
key="qwertyuiopasdfghjkl;zxcvbnm,./"
str=""
if(dir=="R"):
    a=-1
else:
    a=1
for x in seq:
    i=key.index(x)
    str+=key[i+a]
print(str)
    
