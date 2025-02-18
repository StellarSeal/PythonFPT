def is_squared(x: int) -> bool:
    return (int(x ** 0.5) ** 2) == x

def average_squared_digit_pairs(x: int) -> float:
    pair = 0
    total = 0
    count = 0
    while x > 10:
        pair = x % 100
        x //= 10
        if is_squared(pair):
            total += pair
            count += 1
    return float(total / count)

def homework() -> None:
    n = int(input("Nhap vao so n: "))
    average = average_squared_digit_pairs(n)
    print("TBC: %.3f" % average)

if __name__ == "__main__":
    homework()
