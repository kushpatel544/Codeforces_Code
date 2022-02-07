t=int(input())


def func(n,a,b):
    str=""
   
    while(n>=1):
        bb=b
        aa=a
        s=97
        while(aa>=1 and n>=1):
            str+=chr(s)
          
            if(bb>1):
                s+=1
            bb-=1
            aa-=1
            n-=1
        
        
    print(str)

for x in range(t):
    y=input().split()
    n=int(y[0])
    a=int(y[1])
    b=int(y[2])
    func(n,a,b)


    
            
    

        
