n = int(input("Nhap vao so nguyen n: "))

if n <= 3:
    print(n, 'khong phai la so ban nguyen to')
else:
    m = 0
    for i in range(int(n ** 0.5) + 1, 1, -1):
        div_dint = 0
        for x in range(2, int(i ** 0.5) + 1):
            if i % x == 0:
                div_dint += 1
                break
        if div_dint > 0:
            continue
        if n % i == 0:
            out = n // i
            div_bint = 0
            for k in range(2, int(out ** 0.5) + 1):
                if out % k == 0:
                    div_bint += 1
                    break
            if div_bint == 0:
                print(n, "la so ban nguyen to!")
                m += 1
                break
    if m == 0:
        print(n, "khong phai la so ban nguyen to!")
    
