def gcd_euclid(a,b):
    if(b==0):
        return a
    else:
        x,y=b,a%b
        return gcd_euclid(x,y)

n=int(input("enter first number:"))
m=int(input("enter second number:"))

print(gcd_euclid(n,m))
