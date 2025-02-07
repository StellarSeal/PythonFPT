n = int(input("Nhap vao so n: "))

max_pair = 0
previous_digit = -1
while n > 0:
    digit = n % 10
    n //= 10
    if previous_digit < 0:
        previous_digit = digit
        continue
    digit_pair = digit * 10 + previous_digit
    if max_pair < digit_pair:
        max_pair = digit_pair
    previous_digit = digit
print(max_pair)
