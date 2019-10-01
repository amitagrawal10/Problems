t=int(input())
for i in range(1,t+1):
    n=int(input())
    last=n%10
    
    if(n<10):
        first=0
    else:
        while(n>=10):
            n=n//10
        first=n%10
        
    sum1=first+last
    print(sum1)