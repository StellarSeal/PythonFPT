xa = float(input("Nhập tọa độ x(A): "))
ya = float(input("Nhập tọa độ y(A): "))
xb = float(input("Nhập tọa độ x(B): "))
yb = float(input("Nhập tọa độ y(B): "))

d = (((xb - xa) ** 2) + ((yb - ya) ** 2)) ** (1 / 2)

print("Khoảng cách từ A -> B: %.2f" % d)
