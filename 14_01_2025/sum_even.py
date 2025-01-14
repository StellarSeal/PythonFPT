n = int(input("Nhap vao so nguyen n: "))

end = 0

if n % 2 == 0:
   end = n + 1
else:
    end = n

sum_even = 0
for i in range(2, end, 2):
    sum_even += i

print("Tong cac so chan tu 1 - n:", sum_even)
