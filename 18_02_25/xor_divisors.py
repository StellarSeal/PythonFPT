def input_function():
    return [int(input("Nhap vao so nguyen a: ")), int(input("Nhap vao so nguyen b: "))]

def xor_divisors(a, b):
    divisors = []
    for i in range(1, (a + 1)):
        if a % i == 0:
            divisors.append(i)
    for j in range(1, (b + 1)):
        if b % j == 0:
            divisors.append(j)
    xor_divisors = []
    for d in divisors:
        if ((a % d == 0) and (b % d != 0)) or ((a % d != 0) and (b % d == 0)):
            xor_divisors.append(d)
    return xor_divisors

def main():
    input_list = input_function()
    a, b = input_list[0], input_list[1]
    print(xor_divisors(a, b))

if __name__ == "__main__":
    main()
