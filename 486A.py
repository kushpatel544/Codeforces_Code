n=int(input())
if n%2==0:
    n=n//2
    sum1=(n*(2+n*2))//2
    sum2=(n*(1+n*2-1))//2
    sum=sum1-sum2
else:
    sum1=(((n//2)*(2+n-1)))//2

    sum2=(((n+1)*(2+n-1)))//4
  
    sum=sum1-sum2
print(sum)