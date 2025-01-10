a = float(input("Nhap vao canh A: "))
b = float(input("Nhap vao canh B: "))
c = float(input("Nhap vao canh C: "))

is_triangle = (a + b >= c) and (a + c >= b) and (b + c >= a)

print("3 canh nhap vao la cua tam giac:", is_triangle)
