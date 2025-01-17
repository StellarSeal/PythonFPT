n = int(input("Nhap vao so nguyen n: "))

if (n <= 0) or (n > 10):
    print("Invalid")
else:
    for i in range(1, 11):
        print(n, "x", i, "=", (n*i), sep="")
