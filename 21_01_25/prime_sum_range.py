a = int(input("Nhap vao so nguyen a: "))
b = int(input("Nhap vao so nguyen b: "))

total = 0
for k in range(a, (b + 1)):
    if k < 2:
        continue
    ival = 0
    for i in range(2, int(k ** 0.5) + 1):
        if k % i == 0:
            ival += 1
            break
    if ival == 0:
        total += k
print("Tong cac so nguyen to tu ", a, " - ", b, " = ", total, sep = "")
