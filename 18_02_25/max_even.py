def main():
    n = int(input("Nhap vao so nguyen n: "))
    numbers = []
    for i in range(n):
        numbers.append(int(input()))
    max_even = 0
    for x in numbers:
        if (x % 2 == 0) and (max_even < x):
            max_even = x
    print(max_even)

if __name__ == "__main__":
    main()
