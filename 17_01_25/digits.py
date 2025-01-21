n = int(input("Nhap vao so nguyen n: "))
d = int(input("Nhap vao so nguyen d: "))

nlen = 0
dlen = 0
ndupe = n
ddupe = d
while ndupe > 0:
    nlen += 1
    ndupe //= 10
while ddupe > 0:
    dlen += 1
    ddupe //= 10

flag = 0

for i in range(1, (nlen - dlen) + 1):
    ndupe = n % (10 ** (nlen - i))
    for k in range(1, (nlen - dlen - i) + 1):
        ndupe //= 10
        if ndupe == d:
            flag += 1
            break
    if flag != 0:
        break

print(flag != 0)
