def is_squared(x: int) -> bool:
    return (int(x ** 0.5) ** 2) == x

def main_0x1() -> None:
    n = int(input("Nhap vao so n: "))
    previous = -1
    digit_pair = 0
    while n > 0:
        digit = n % 10
        n //= 10
        if previous < 0:
            previous = digit
            continue
        digit_pair = digit * 10 + previous
        previous = digit
        if is_squared(digit_pair):
            print(digit_pair, end=" ")

if __name__ == "__main__":
    main_0x1()
