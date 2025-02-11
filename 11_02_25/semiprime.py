def is_prime(x: int) -> bool:
    if x < 2:
        return False
    for i in range(2, (int(x ** 0.5) + 1)):
        if x % i == 0:
            return False
    return True

def semiprime(x: int) -> bool:
    for i in range(2, (x // 2) + 1):
        if (x % i == 0) and (not is_prime(i)):
            return False
    return True
        

def main_0x2() -> None:
    n = int(input("Nhap vao so n: "))
    print(semiprime(n))

if __name__ == "__main__":
    main_0x2()
