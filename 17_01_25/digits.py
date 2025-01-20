n = int(input("Nhap vao so nguyen n: "))
d = int(input("Nhap vao so nguyen d: "))

nlen = 0
ndupe = n
while ndupe > 0:
    nlen += 1
    ndupe //= 10
nred = n
ndupe = n
cflag = 0
for i in range(1, (nlen + 1)):
    ndupe = nred
    ndupe //= 10
    if ndupe == d:
        cflag += 1
        break
    else:
        ndupe = nred
    ndupe %= (10 ** (nlen - i))
    if ndupe == d:
        cflag += 1
        break
    nred //= 10
print(cflag > 0)
