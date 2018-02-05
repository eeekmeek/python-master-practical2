# Computing the greatest common divisor

def gcd(n1,n2):
    if(n2==0):
        return n1
    else:
        return gcd(n2,n1%n2)
n1=int(input("Enter first integer:"))
n2=int(input("Enter second integer:"))
GCD=gcd(n1,n2)
print("GCD is: ")
print(GCD)
