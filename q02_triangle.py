# check validity
def check(a,b,c,p):
    if p - a <= a:
        return False
    elif p - b <= b:
        return False
    elif p - c <= c:
        return False
    else:
        return True

# initialisation
a = int(input("Enter side 1: "))
b = int(input("Enter side 2: "))
c = int(input("Enter side 3: "))

p = a + b + c # perimeter

if check(a,b,c,p):
    print("Perimeter = ", p)
else:
    print("Invalid triangle")
