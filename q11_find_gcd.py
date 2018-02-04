# Computing the greatest common divisor

def gcd(n1, n2):
    gcd = 1
    
    if n1 % n2 == 0:
        return n2
    
    for k in range(int(n2 / 2), 0, -1):
        if n1 % n2 == 0 and n2 % k == 0:
            gcd = k
            break  
    return gcd

print(gcd(12, 17))
print(gcd(4, 6))
