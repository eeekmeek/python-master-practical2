# Finding the factors of an integer

N = int(input("Enter integer: "))
i = 2 
first = True 

while (N >= i):
    if (N % i == 0):  
        N /= i # N = N/i 
        if first == True:
            print(i, end='')
            first = False  
        else:
            print(',', i, end='') 
    else:
        i += 1   

print()
