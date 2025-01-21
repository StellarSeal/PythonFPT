n = int(input("Nhap vao so nguyen n: "))

print("Cac so hoan hao tu 1 -", n, "= ", end="")
for i in range(1, (n + 1)):
    div_sum = 0
    for j in range(1, ((i // 2) + 1)):
        if i % j == 0:
            div_sum += j
    if div_sum == i:
        print(i, end=" ")
