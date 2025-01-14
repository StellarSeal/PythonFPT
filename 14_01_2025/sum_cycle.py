n = int(input("Nhap vao so nguyen n: "))

total_cyc = 0

for i in range(1, (n + 1)):
    if i % 2 != 0:
        total_cyc += i
    else:
        total_cyc -= i

print("Tong uoc so cua", n, "=", total_cyc)
