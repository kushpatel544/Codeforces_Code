n=input()
a=n.split("WUB")
str=""
for x in a:
    if(x!=""):
        str=str+x+" "
print(str.strip())