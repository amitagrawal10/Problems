t=int(input())
for i in range(1,t+1):
    n=int(input())
    sum1=0
    if(n<10):
        sum1=0
    else:
        while(n>=10):
            sum1=sum1+n%10
            
            n=n//10
        sum1=sum1+n
    print(sum1)