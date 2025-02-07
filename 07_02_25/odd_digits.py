n = int(input("Nhap vao so n: "))

even = 0
while n > 0:
    if n % 20 == 0:
        even += 1
        break
    n //= 10
print(even == 0)
