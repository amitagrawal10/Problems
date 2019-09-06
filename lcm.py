def gcd_euclid(a,b):
    if(b==0):
        return a
    else:
        x,y=b,a%b
        return gcd_euclid(x,y)

def lcm(a,b):
    lcm=(a*b)/gcd_euclid(a,b)
    return lcm


n=int(input("enter first number:"))
m=int(input("enter second number:"))

print(lcm(n,m))
