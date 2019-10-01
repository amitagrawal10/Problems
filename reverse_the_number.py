t=int(input())
for i in range(1,t+1):
    n=int(input())
    list1=[]
    if(n<10):
        print(10)
    else:
        while(n>=10):
            digit=n%10
            list1.append(digit)
            n=n//10
        last_digit=n
        list1.append(last_digit)
    
    mul=1
    ans=0
    for i in range(len(list1),0,-1):
        
        ans=ans+ list1[i-1]*mul
        
        mul*=10
    print(ans)
