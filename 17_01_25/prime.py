print("Section A - Prime check of a single integer")

n = int(input("Nhap vao so nguyen to n: "))

fval = 0
for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
        fval += 1
        break
if fval > 0:
    print(n, "khong phai la so nguyen to")
else:
    print(n, "la so nguyen to")
    

# Can't use sieve prime listing because we haven't gotten to working with arrays :)
print("Section B - Prime listing in a specified range")

n = int(input("Nhap vao so nguyen n: "))

print("Cac so nguyen to tu 1 - ", n, ": ", sep="", end="")

for k in range(2, (n + 1)):

    ival = 0
    for i in range(2, int(k ** 0.5) + 1):
        if k % i == 0:
            ival += 1
            break
    if ival == 0:
        print(k, end=" ")
    
