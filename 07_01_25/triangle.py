a = float(input("Nhập cạnh A: "))
b = float(input("Nhập cạnh B: "))
c = float(input("Nhập cạnh C: "))

P = a + b + c
HP = P / 2
S = (HP * (HP - a) * (HP - b) * (HP - c)) ** (1 / 2)

print("Chu vi hình tam giác:", P)
print("Diện tích hình tam giác:", S)
