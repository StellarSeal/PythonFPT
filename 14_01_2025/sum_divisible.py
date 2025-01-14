n = int(input("Nhap vao so nguyen n: "))

total_div = 0

for i in range(1, (n + 1)):
    if n % i == 0:
        total_div += i

print("Tong uoc so cua", n, "=", total_div)
