n = int(input("Nhap vao so n: "))

unordered = 0
previous_mod = 10
while n > 0:
    if previous_mod <= (n % 10):
        unordered += 1
        break
    previous_mod = n % 10
    n //= 10
print(unordered == 0)
